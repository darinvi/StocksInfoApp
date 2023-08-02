from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

UserModel = get_user_model()

class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True
    )

class Ticker(models.Model):
    ticker_name = models.CharField(
        max_length=6,
        blank=False,
        null=False
    )
    trade_strategy = models.TextField(
        blank=False,
        null=False
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    show_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Comment(models.Model):
    comment = models.TextField(blank=False, null=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    resources = models.URLField(null=False, blank=False)
    picture = models.URLField(null=True, blank=True)