import socket

from django.shortcuts import render
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


def main(request):
    form = SentimentForm()
    template = "livesentiment/main.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@csrf_exempt
def get_value(request):
    # This is where the magic should happen
    text = request.POST["text"]
    print("Yo")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.101", 8095))
        s.send(text.encode("utf-8"))
        rec = s.recv(1024).decode("utf-8")
    except Exception:
        return HttpResponse("Service is unavailable at the moment. Tell Mårten to start it if you want to try it out.")

    answer = '{}: {}'.format(text, rec)
    return HttpResponse(answer)


class SentimentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="")
