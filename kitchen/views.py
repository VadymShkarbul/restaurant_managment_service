from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType


def index(request):
    num_cooks = Cook.objects.count()
    num_dish_type = DishType.objects.count()
    num_dish = Dish.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dish_type": num_dish_type,
        "num_dish": num_dish,
    }

    return render(request, "kitchen/index.html", context=context)
