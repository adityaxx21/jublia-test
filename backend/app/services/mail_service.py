from flask import current_app as app
from flask_mail import Message

class MailService:
    def send_email(mail_sender, mail_recipient, mail_subject, mail_content):
        try:
            msg = Message(
                subject = mail_subject, 
                sender = mail_sender, 
                recipients = mail_recipient, 
                body = mail_content
            )
            mail = app.extensions.get('mail')
            mail.send(msg)
            app.logger.info("Mail sent")
            return "Mail sent successfully"
        except Exception as e:
            app.logger.info("Mail not sent: ", e)
            return "Mail not sent"
            

