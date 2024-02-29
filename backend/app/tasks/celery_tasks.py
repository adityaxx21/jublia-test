
from celery import shared_task
from time import sleep
import datetime
from app.services.mail_service import MailService
from app.models.models import db, Email, Recipient
from helper.helpers import get_utc_plus_8

mail_service = MailService

@shared_task(ignore_result=False)
def long_running_task(iterations) -> int:
    result = 0
    for i in range(iterations):
        result += i
        print(result)
        sleep(2) 
    return result 

@shared_task()
def periodic_task():
    try:
        emails = Email.query.filter(db.and_(Email.deleted_at == None, Email.timestamp <= get_utc_plus_8())).all()
        if emails:
            for email in emails:
                recipient_dict_list = [rec.email for rec in Recipient.query.filter_by(deleted_at=None).all()]
                mail_service.send_email(
                    mail_content = email.email_content,
                    mail_subject = email.email_subject,
                    mail_recipient = recipient_dict_list,
                    mail_sender = "adityayatma@gmail.com"
                )
                email.deleted_at = get_utc_plus_8()
                db.session.commit()
                print(f"Mail Successfully at {datetime.datetime.now()}")
        else:
            print("Data Not Found")
    except db.exc.SQLAlchemyError as e:
            print(f"An Error Occured {e}")
