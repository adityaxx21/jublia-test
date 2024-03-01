from marshmallow import Schema, fields, validate
from helper.helpers import get_utc_plus_8

class EmailSchema(Schema):
    id = fields.Integer(dump_only=True)
    event_id = fields.Integer(required=True)
    email_subject = fields.String(required=True, validate=validate.Length(max=100))
    email_content = fields.String(required=True)
    timestamp = fields.DateTime(required=True)
    deleted_at = fields.DateTime(allow_none=True)
    
class RecipientSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String(required=True, validate=validate.Email())
    deleted_at = fields.DateTime(allow_none=True)