from django import forms
from django.contrib.auth.models import User

from NoSolo.main.helpers import MyFormMixin


class LoginForm(MyFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    username = forms.CharField(
        label=u'Username',
        required=True,
    )
    password = forms.CharField(
        label=u'Password',
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'password']
