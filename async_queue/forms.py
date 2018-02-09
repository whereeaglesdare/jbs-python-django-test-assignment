from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .tasks import send_http_request_task


class SendForm(forms.Form):
    delay_sec = forms.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def send_request(self):
        send_http_request_task.delay(self.cleaned_data['delay_sec'])