
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class Index(TemplateView):

    template_name = "index.html"

    def post(self, form):
        send_mail(
            form.POST['subject'],
            "De la part de "+form.POST['name']+"\n"+form.POST['message'],
            form.POST['email'],
            ['guillaumeferreira00@gmail.com'],
        )
        return HttpResponseRedirect(reverse_lazy("index"))


class Saur(TemplateView):

    template_name = "saur.html"