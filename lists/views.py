from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login/")
def lists_main(request):
    template = "lists/main.html"
    context = {
        "user": request.user,
        "lists": ["Grocery list", "Important list", "Other list"],
    }
    return render(request, template, context)
