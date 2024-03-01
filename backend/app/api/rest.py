from flask import Blueprint, jsonify, request
from app.models.models import db, Email, Recipient
from app.services.mail_service import MailService
from helper.helpers import get_utc_plus_8
from sqlalchemy.exc import IntegrityError
from app.schemas.schemas import EmailSchema, RecipientSchema
from marshmallow import ValidationError
from app.config import mail_sender
from .base_rest import BaseRest

email_schema = EmailSchema()
recipient_schema = RecipientSchema()
base_rest  = BaseRest()


api = Blueprint('api', __name__)
email_service = MailService

@api.get('/get_emails')
def get_emails():
    emails = Email.query.filter_by(deleted_at=None).all()
    return base_rest.get_response_object(200, [email.serialize() for email in emails])

@api.post('/save_emails')
def create_task():
    data = request.get_json()
    try:
        email = email_schema.load(data)
        email['created_at'] = get_utc_plus_8()
        email['updated_at'] = get_utc_plus_8()
        
        save = Email(**email) 
        db.session.add(save)
        db.session.commit()
        return base_rest.get_response_object(201,  email)
    except ValidationError as err:
        return base_rest.get_response_object(400,  err.messages)


@api.post('/send_mail/<id>')
def send_mail(id: int):
    try:
        email = Email.query.filter(db.and_(Email.deleted_at == None, Email.id == id)).one()
        if email:
            recipient_dict_list = [rec.email for rec in Recipient.query.filter_by(deleted_at=None).all()]
            response = email_service.send_email(
                mail_content = email.email_content,
                mail_subject = email.email_subject,
                mail_recipient = recipient_dict_list,
                mail_sender = mail_sender
            )
            email.deleted_at = get_utc_plus_8()
            db.session.commit()
            return base_rest.get_response_object(201, response)
        else:
            return base_rest.get_response_object(404)
    except db.exc.SQLAlchemyError as e:
            return base_rest.get_response_object(500, e)

@api.post('/recipient')
def save_recipient():
    data = request.get_json()
    try:
        recipient = recipient_schema.load(data)
        recipient['created_at'] = get_utc_plus_8()
        recipient['updated_at'] = get_utc_plus_8()
        new_recipient = Recipient(**recipient)
        
        db.session.add(new_recipient)
        db.session.commit()
        return base_rest.get_response_object(201, new_recipient.serialize())
    except IntegrityError:
        db.session.rollback()
        return base_rest.get_response_object(400, 'Email already exists')

@api.get('/recipient')
def get_recipients():
    recipients = Recipient.query.filter_by(deleted_at=None).all()
    return base_rest.get_response_object(200, [recipient.serialize() for recipient in recipients])

@api.get('/recipient/<int:id>')
def get_recipient(id):
    recipient = Recipient.query.filter_by(deleted_at=None, id=id).first()
    return base_rest.get_response_object(200, recipient.serialize())
    
@api.put('/recipient/<int:id>')
def update_recipient(id):
    recipient = Recipient.query.get(id)

    if not recipient:
        return base_rest.get_response_object(404)

    data = request.get_json()

    try:
        data_recipient = recipient_schema.load(data)
        recipient.email =  data_recipient['email']
        recipient.updated_at = get_utc_plus_8()
        db.session.commit()
        return base_rest.get_response_object(201, recipient.serialize())
    except IntegrityError:
        db.session.rollback()
        return base_rest.get_response_object(400, 'Email already exists')

@api.delete('/recipient/<int:id>')
def delete_recipient(id):
    recipient = Recipient.query.get(id)

    if not recipient:
        return base_rest.get_response_object(404)

    recipient.deleted_at = get_utc_plus_8()
    recipient.updated_at = get_utc_plus_8()
    db.session.commit()
    return base_rest.get_response_object(200, 'Recipient deleted successfully')