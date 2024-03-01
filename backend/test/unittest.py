import unittest
from app import create_app
from app.models.models import db, Email, Recipient
from app.services.mail_service import MailService
from helper.helpers import get_utc_plus_8
from marshmallow import ValidationError
from app.schemas.schemas import EmailSchema, RecipientSchema
from app.config import mail_sender

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        # Create test data in a way that is isolated and doesn't affect other tests
        with self.app.app_context():
            db.create_all()
            self.email = Email(
                email_subject="Test Email Subject",
                email_content="Test Email Content",
                created_at=get_utc_plus_8(),
                updated_at=get_utc_plus_8()
            )
            db.session.add(self.email)
            db.session.commit()

            self.recipient = Recipient(
                email="test@example.com",
                created_at=get_utc_plus_8(),
                updated_at=get_utc_plus_8()
            )
            db.session.add(self.recipient)
            db.session.commit()

    def tearDown(self):
        with self.app.app_context():
            db.session.query(Email).delete()
            db.session.query(Recipient).delete()
            db.session.commit()
            db.drop_all()

    def test_get_emails(self):
        response = self.client.get('/get_emails')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)  # Check for expected number of emails
        self.assertEqual(data[0]['email_subject'], self.email.email_subject)

    def test_create_email_valid_data(self):
        data = {
            "email_subject": "New Email",
            "email_content": "This is a new email content"
        }
        response = self.client.post('/save_emails', json=data)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)  # Check for presence of ID in response

    def test_create_email_invalid_data(self):
        data = {}  # Missing required fields
        response = self.client.post('/save_emails', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.get_json())  # Check for validation errors

    def test_send_mail_existing_email(self):
        # Assuming email_service.send_email is mocked or returns a success response
        response = self.client.post('/send_mail/1')
        self.assertEqual(response.status_code, 201)
        # Check for expected response content based on mock or actual implementation

    def test_send_mail_nonexistent_email(self):
        response = self.client.post('/send_mail/100')  # Invalid ID
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

    def test_get_recipients(self):
        response = self.client.get('/recipient')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)  # Check for expected number of recipients
        self.assertEqual(data[0]['email'], self.recipient.email)

    def test_get_recipient_existing(self):
        response = self.client.get('/recipient/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['email'], self.recipient.email)
        
    def test_get_recipient_nonexistent(self):
        response = self.client.get('/recipient/2')  # Nonexistent ID
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

    def test_update_recipient_valid_data(self):
        data = {"email": "updated_email@example.com"}
        response = self.client.put('/recipient/1', json=data)
        self.assertEqual(response.status_code, 201)
        data = self.client.get('/recipient/1').get_json()
        self.assertEqual(data['email'], "updated_email@example.com")

    def test_update_recipient_invalid_data(self):
        data = {}  # Missing required fields
        response = self.client.put('/recipient/1', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('errors', response.get_json())  # Check for validation errors

    def test_update_recipient_nonexistent(self):
        data = {"email": "new_email@example.com"}
        response = self.client.put('/recipient/2', json=data)  # Nonexistent ID
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())

    def test_delete_recipient_existing(self):
        response = self.client.delete('/recipient/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/recipient/1')
        self.assertEqual(response.status_code, 404)  # Check if recipient is deleted

    def test_delete_recipient_nonexistent(self):
        response = self.client.delete('/recipient/2')  # Nonexistent ID
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.get_json())
