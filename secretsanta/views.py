from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import random
import copy

# Create your views here.


def main(request):
    template = "secretsanta/main.html"
    form = SantaForm()
    context = {"form": form}
    if request.method == "POST":
        form = SantaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data["name"])
            context["message"] = find_person(data["name"], data["code"])
    return render(request, template, context)


def find_person(name, code):
    random.seed(71)
    names = ["Ruth", "Gabriella", "Giedre", "Pappa", "Mamma", "Arturas"]
    codes = ["goflojo", "bananhej", "blarvas", "FtR887vgspae", "runhej", "internet"]

    if name.strip() not in names:
        return "Sluta hitta på falska namn"

    secret_names = names.copy()
    unique = False
    while not unique:
        unique = True
        random.shuffle(secret_names)
        for index, n in enumerate(secret_names):
            if n == names[index]:
                unique = False

    # Verification
    index = names.index(name.strip())
    if code.strip() == codes[index]:

        return secret_names[index]
    return None


class SantaForm(forms.Form):
    name = forms.CharField(label="Ditt namn", max_length=100)
    code = forms.CharField(label="Kod", max_length=100)
