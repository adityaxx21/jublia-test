from sqlalchemy import Column, Integer, String, TIMESTAMP, UnicodeText
from flask_sqlalchemy import SQLAlchemy
from helper.helpers import get_utc_plus_8
from marshmallow import Schema, fields, ValidationError

db = SQLAlchemy()

class Email(db.Model):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    email_subject = Column(String(100), unique=True, nullable=False)
    email_content = Column(String, unique=True, nullable=False)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,  default=get_utc_plus_8())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default=get_utc_plus_8(), onupdate = get_utc_plus_8())
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'email_subject': self.email_subject,
            'email_content': self.email_content,
            'timestamp': self.timestamp,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
        
class Recipient(db.Model):
    __tablename__ = 'recipients'
    id = Column(Integer, primary_key=True)
    email = Column(UnicodeText, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,  default=get_utc_plus_8())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default=get_utc_plus_8(), onupdate = get_utc_plus_8())
    deleted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    

