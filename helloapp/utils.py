from django.conf import settings
from django.core.mail import send_mail
import string
import random

def send_mail_to_user(recipient_list,subject,message):
    ''' recipient list contains list of emails for sending mail, so does subject and message'''
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, recipient_list )


def randomstring(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length)) 