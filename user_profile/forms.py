from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class MyDateInput(forms.DateInput):


    class Media:
        extend = False
        css = {'all': ( 'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.7.1/css/bootstrap-datepicker.css',) }
        js = ( 'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.7.1/js/bootstrap-datepicker.js',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'contacts', 'birth_date', 'profile_photo')
        widgets = {
            'birth_date': MyDateInput(attrs={'class': 'form-control datepicker', "data-toggle": "datepicker"}, format='%d-%m-%Y')
        }