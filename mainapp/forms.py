from django import forms
from django.core.validators import EmailValidator, MinLengthValidator   # Pochta manzilni validatsiya holatini tekshiradi
from django.core.exceptions import ValidationError                      # Hatolik haqida habr beradi
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50, validators=[
        UnicodeUsernameValidator()
    ])
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.CharField(max_length=255, widget=forms.EmailInput, validators=[
        EmailValidator(message="Pochta manzil notog'gri")   # Agar hato bo'lsa shunday yozuv chiqadi
    ])
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def clean_confirm(self):  # confirm polyasini validatsiyadan o'tkazadi
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas")

        return self.cleaned_data['confirm']

    def clean_username(self):
        # self.cleaned_data['username'] = self.cleaned_data['username'].lower()
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise ValidationError("Siz kiritgan 'Username' allaqachon mavjud")

        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Siz kiritgan email mavjud")
        return email