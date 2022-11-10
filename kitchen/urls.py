from django.urls import path

from kitchen.views import index, DishTypeListView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("dishes_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes_types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishes_types/delete/<int:pk>/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
]

app_name = "kitchen"
