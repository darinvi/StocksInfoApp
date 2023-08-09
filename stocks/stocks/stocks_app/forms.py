from .models import Ticker, Comment, Course
from django import forms

class TickerModelForm(forms.ModelForm):
    class Meta:
        model = Ticker
        exclude = ['user']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['ticker', 'author', 'created_at']

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['author', ]
