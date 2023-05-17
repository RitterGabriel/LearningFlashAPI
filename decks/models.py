from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime

class Deck(models.Model):
    name = models.CharField(max_length=40, null=False)
    description = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FlashCard(models.Model):
    phrase = models.CharField(max_length=80, null=False)
    translated_phrase = models.CharField(max_length=80, null=False)
    last_time_checked = models.DateTimeField(null=False, auto_now_add=True)
    domain_level = models.IntegerField(null=False, default=0)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
