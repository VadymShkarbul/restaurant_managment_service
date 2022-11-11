from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, CookYOEUpdateForm, DishForm
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishes_types_list"
    template_name = "kitchen/dishes_types_list.html"
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookYOEUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookYOEUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
