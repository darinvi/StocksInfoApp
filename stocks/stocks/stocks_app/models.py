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
    trade_strategy = models.CharField(
        blank=False,
        null=False
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    show_public = models.BooleanField()

class Comment(models.Model):
    comment = models.CharField(
        blank=False,
        null=False
    )
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.localtime(timezone.now())
        super().save(*args, **kwargs)