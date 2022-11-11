from django.urls import path

from kitchen.views import (index,
                           DishTypeListView,
                           DishTypeCreateView,
                           DishTypeUpdateView,
                           DishTypeDeleteView,
                           DishDetailView,
                           DishListView,
                           DishCreateView,
                           DishUpdateView,
                           DishDeleteView,
                           CookListView,
                           CookDetailView,
                           CookCreateView,
                           CookYOEUpdateView,
                           CookDeleteView, add_remove_dish, )


class CookUpdateView:
    pass


urlpatterns = [
    path("", index, name="index"),
    path("dishes_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dishes_types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dishes_types/delete/<int:pk>/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/delete/<int:pk>/", DishDeleteView.as_view(), name="dish-delete"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/update/<int:pk>/", CookYOEUpdateView.as_view(), name="cook-update"),
    path("cooks/delete/<int:pk>/", CookDeleteView.as_view(), name="cook-delete"),
    path("dishes/add_remove_dish/<int:pk>/", add_remove_dish, name="add_remove_dish"),
]

app_name = "kitchen"
