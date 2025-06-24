#Sending mail to the users who just regestered useing celery

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    send_mail(
        subject="Welcome to DjangoTask!",
        message="Thank you for registering.",
        from_email="vedanjyadav@gmail.com",
        recipient_list=[email],
    )
