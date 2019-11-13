from django.forms import ModelForm, Form
from chat.models import Message


class CreateNewMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['content', ]
