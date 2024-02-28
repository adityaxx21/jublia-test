from celery import shared_task
from datetime import datetime, timedelta

# @shared_task(ignore_result=False)
# def my_periodic_task():
#     print("Executing task every 5 minutes")
#     # Add your task logic here

# # Define periodic task schedule
# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, my_periodic_task.s(), name='execute-every-5-minutes')

@shared_task(ignore_result=False)
def add_together(a: int, b: int) -> int:
    return a + b