from .models import Ticker, Comment
from django import forms

class TickerModelForm(forms.ModelForm):
    class Meta:
        model = Ticker
        exclude = ['user']

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['ticker', 'author', 'created_at']

