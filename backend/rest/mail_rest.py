from flask import Blueprint, jsonify, request
from model.models import db, Email, Recipient
from service.mail_service import MailService
from tasks.tasks import add_together
from helper.helpers import get_utc_plus_8

api = Blueprint('api', __name__)
email_service = MailService

@api.get('/get_emails')
def get_emails():
    emails = Email.query.filter_by(deleted_at=None).all()
    result = add_together.delay(10, 20)
    print(result)
    return jsonify([email.serialize() for email in emails])

@api.post('/save_emails')
def create_task():
    data = request.json
    email = Email(**data) 
    db.session.add(email)
    db.session.commit()
    return jsonify(email.serialize()), 201


# change this later
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
                mail_sender = "adityayatma@gmail.com"
            )
            email.deleted_at = get_utc_plus_8()
            db.session.commit()
            return response, 201
        else:
            return "No result found for name:", 404
    except db.exc.SQLAlchemyError as e:
        return "An error occurred: {}".format(e), 505
