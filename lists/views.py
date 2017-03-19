from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
        "friends": request.user.profile.friends.all(),
        "lists": request.user.shared_lists.all(),
    }
    return render(request, template, context)


@login_required(login_url="/login/")
def get_items(request, list_id):
    mn_list = get_object_or_404(MnList, id=list_id)
    items = MnItem.objects.filter(list=mn_list)

    data = serializers.serialize("json", items)

    return HttpResponse(data)


@csrf_exempt
@login_required(login_url="/login/")
def save_items(request, list_id):
    if request.method == "POST":
        if list_id == "0":
            name = request.POST["mn_name"]
            mn_list = MnList(name=name, user=request.user)
            mn_list.save()
            mn_list.shared_width.add(request.user)
            mn_list.save()
        else:
            mn_list = get_object_or_404(MnList, id=list_id)

        items = MnItem.objects.filter(list=mn_list)
        items.delete()

        for key in request.POST:
            if key == "mn_name":
                continue
            item = MnItem(list=mn_list, name=key, active=(request.POST[key] == 'true'))
            item.save()

    return HttpResponse("success")


@csrf_exempt
@login_required(login_url="/login/")
def remove_list(request, list_id):
    mn_list = get_object_or_404(MnList, id=list_id)
    mn_list.delete()
    return HttpResponse("success")


@login_required(login_url="/login/")
@csrf_exempt
def share_list(request, list_id):
    # Shares list with friends
    if request.method == "POST":
        username = request.POST["friend"]
        user = get_object_or_404(User, username=username)
        mn_list = get_object_or_404(MnList, id=list_id)
        mn_list.shared_width.add(user)
        return HttpResponse("success")
    return HttpResponse("Vad gör du här?")




