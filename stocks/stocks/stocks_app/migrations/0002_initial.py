# Generated by Django 4.2.3 on 2023-07-27 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks_app', '0001_initial'),
        ('stocks_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_name', models.CharField(max_length=6)),
                ('trade_strategy', models.CharField()),
                ('show_public', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks_app.ticker'),
        ),
    ]