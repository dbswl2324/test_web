from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICE_CLASS = (('subscribed', 'subscribed'), ('unsubscribed', 'unsubscribed'))

class Member(AbstractUser):
    nickname = models.CharField(max_length=100)
    userclass = models.CharField(
        max_length=50,
        choices=CHOICE_CLASS, 
        default='unsubscribed',
    )