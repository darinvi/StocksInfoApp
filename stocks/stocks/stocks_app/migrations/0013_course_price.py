# Generated by Django 4.2.3 on 2023-08-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_app', '0012_alter_course_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]