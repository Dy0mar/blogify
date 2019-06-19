# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def mailing(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
