from django.forms import ModelForm
from django import forms
from .models import *


class MessageForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Написать сообщение...',
                'class': 'p-4 text-black',
                'maxlength': '300', 'autofocus': True,
            }),
        }


class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name',]
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'placeholder': 'Добавить название...',
                'class': 'p-4 text-black',
                'maxlength': '300', 'autofocus': True,
            }),
        }
