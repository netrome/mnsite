import random

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Dish
from .forms import DishForm
from .security import is_safe

# Create your views here.


def random_dish():
    dishes = Dish.objects.all()

    if len(dishes) == 0:
        return None

    i = random.randint(0, len(dishes) - 1)
    return dishes[i]


def main_view(request):

    if request.method == "POST":
        f = DishForm(request.POST)
        if f.is_valid():
            f.clean()
            if is_safe(f):
                f.save()

    dish = random_dish()
    dish_form = DishForm()
    context = {
        "dish": dish,
        "dishes": Dish.objects.all(),
        "dish_form": dish_form,
        }
    template = "foodlist/showfood.html"
    return render(request, template, context)


@csrf_exempt
def ajax(request):

    question = request.POST["question"]
    dish = random_dish()
    answer = '<h3 id="dish-name">{0}</h3><p id="dish_info">{1}</p>'.format(dish.name, dish.description)

    return HttpResponse(answer)
