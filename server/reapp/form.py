from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from reapp.models import Text


class RegistrationUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = "__all__"
