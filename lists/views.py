from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import MnList, MnItem

# Create your views here.


@login_required(login_url="/login/")
def lists_main(request):
    template = "lists/main.html"
    context = {
        "user": request.user,
        "lists": MnList.objects.filter(user=request.user),
    }
    return render(request, template, context)


def get_items(request, list_id):
    mn_list = get_object_or_404(MnList, id=list_id)
    items = MnItem.objects.filter(list=mn_list)

    data = serializers.serialize("json", items)

    return HttpResponse(data)


@csrf_exempt
def save_items(request, list_id):
    if request.method == "POST":
        mn_list = get_object_or_404(MnList, id=list_id)
        items = MnItem.objects.filter(list=mn_list)
        items.delete()

        for key in request.POST:
            item = MnItem(list=mn_list, name=key, active=(request.POST[key] == 'true'))
            item.save()

    return HttpResponse("success")
