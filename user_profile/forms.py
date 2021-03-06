from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class MyDateInput(forms.DateInput):
    input_type =  'date'
    attrs = {'class': 'hasDatepicker'}


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'contacts', 'birth_date', 'profile_photo')
        widgets = {
            'birth_date': MyDateInput(),
        }