# Generated by Django 4.2.3 on 2023-08-02 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_app', '0009_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='trade_strategy',
            field=models.TextField(),
        ),
    ]