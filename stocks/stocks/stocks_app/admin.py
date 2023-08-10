from django.contrib import admin
from .models import Ticker, Comment, Course, Profile, Transaction
# Register your models here.

admin.site.register(Ticker)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(Transaction)
