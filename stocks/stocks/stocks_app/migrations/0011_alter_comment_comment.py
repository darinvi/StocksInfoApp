# Generated by Django 4.2.3 on 2023-08-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_app', '0010_alter_ticker_trade_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
