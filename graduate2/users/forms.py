from django.contrib.auth.forms import UserCreationForm

from .models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserPhoneForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('phone_number', 'password1', 'password2')
