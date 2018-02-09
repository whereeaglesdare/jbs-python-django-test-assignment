from django.views.generic.edit import FormView
from .forms import SendForm


class SendView(FormView):
    template_name = 'async_queue/httpbin_send.html'
    form_class = SendForm
    success_url = '/send'

    def form_valid(self, form):
        form.send_request()
        return super(SendView, self).form_valid(form)