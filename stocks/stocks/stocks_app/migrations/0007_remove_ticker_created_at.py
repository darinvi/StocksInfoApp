# Generated by Django 4.2.3 on 2023-07-28 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_app', '0006_alter_comment_created_at_alter_ticker_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticker',
            name='created_at',
        ),
    ]
