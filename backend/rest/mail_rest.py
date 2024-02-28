from flask import Blueprint, jsonify, request
from model.models import db, Email, Recipient

api = Blueprint('api', __name__)

@api.route('/get_emails', methods=['GET'])
def get_emails():
    emails = Email.query.filter_by(deleted_at=None).all()
    return jsonify([email.serialize() for email in emails])

@api.route('/save_emails', methods=['POST'])
def create_task():
    data = request.json
    email = Email(**data) 
    db.session.add(email)
    db.session.commit()
    return jsonify(email.serialize()), 201