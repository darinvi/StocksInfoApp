# Generated by Django 4.2.3 on 2023-07-28 14:25

from django.db import migrations, models
import  django.utils.timezone 

class Migration(migrations.Migration):

    dependencies = [
        ('stocks_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]