from django import forms

from allauth.account.forms import (
        SignupForm,
        LoginForm,
    )
from allauth.utils import set_form_field_order

from users.models import MyUser


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["first_name"] = forms.CharField(
            label="Имя",
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Введите имя'
                }
            )
        )
        self.fields["last_name"] = forms.CharField(
            label="Фамилия",
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Введите фамилию'
                }
            )
        )
        self.fields["email"] = forms.EmailField(
            label="Адрес электронной почты",
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Введите адрес эл. почты'
                }
            )
        )
        self.fields["password1"] = forms.CharField(
            label="Пароль",
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Введите пароль'
                }
            )
        )
        self.fields["password2"] = forms.CharField(
            label="Подтверждение пароля",
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Подтвердите пароль'
                }
            )
        )

        set_form_field_order(self, ['first_name', 'last_name', 'email', 'password1', 'password2'])


class CustomLoginForm(LoginForm):
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control py-4',
                'placeholder': 'Введите пароль'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['login'] = forms.EmailField(
            label="Адрес электронной почты",
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control py-4',
                    'placeholder': 'Введите адрес эл. почты'
                }
            )
        )


class ChangeProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'image', 'email']
