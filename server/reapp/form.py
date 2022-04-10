from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, URLField
from django.core.validators import ValidationError
from reapp.models import Text, Font


class RegistrationUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = "__all__"


class FontForm(ModelForm):
    class Meta:
        model = Font
        fields = "__all__"
    def validateUrl(url):
        url_form_field = URLField()
        try:
            url = url_form_field.clean(url)
        except ValidationError:
            return False
        return True



