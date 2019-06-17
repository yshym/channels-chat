from django import forms
from django.contrib.auth import get_user_model
from slugify import slugify


from .models import (
    Room,
    Message,
)


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'content',
        )


class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            'name',
            'slug'
        )
