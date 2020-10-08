from django import forms
from .models import URL
from django.core.validators import URLValidator


class URLForm(forms.ModelForm):
    user_url = forms.CharField(validators=[URLValidator(message='Invalid URL!')],
                               required=True,
                               max_length=150,
                               widget=forms.TextInput(attrs={
                                   'size': 40,
                                   'placeholder': 'Please paste Your URL here',
                               }))

    class Meta:
        model = URL
        fields = ['user_url']