from django.urls import path

from kitchen.views import (index,
                           DishTypeListView,
                           DishTypeCreateView,
                           DishTypeUpdateView,
                           DishTypeDeleteView, DishListView, DishCreateView, DishUpdateView, DishDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("dishes_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes_types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishes_types/delete/<int:pk>/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/delete/<int:pk>/", DishDeleteView.as_view(), name="dish-delete"),
]

app_name = "kitchen"
