# Generated by Django 4.2.3 on 2023-07-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_app', '0004_alter_comment_created_at_alter_ticker_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
