from django.db import models

CHOICE_CLASS = ((1, 'subscribed'), (0, 'unsubscribed'))

class Member(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_pw = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_class = models.IntegerField(choices = CHOICE_CLASS)
# Create your models here.
