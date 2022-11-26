from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish

DISH_TYPE_LIST_VIEW_URL = reverse("kitchen:dish-type-list")
DISH_LIST_VIEW_URL = reverse("kitchen:dish-list")
COOK_LIST_VIEW_URL = reverse("kitchen:cook-list")


class UnauthorisedGetAccessCheck(TestCase):
    def test_dish_type_list_view_login_required(self):
        response = self.client.get(DISH_TYPE_LIST_VIEW_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_dish_list_view_login_required(self):
        response = self.client.get(DISH_LIST_VIEW_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_cook_list_view_login_required(self):
        response = self.client.get(COOK_LIST_VIEW_URL)
        self.assertNotEqual(response.status_code, 200)

    def test_dish_type_detail_view_login_required(self):
        response = self.client.get(reverse("kitchen:dish-detail", args=[1]))
        self.assertNotEqual(response.status_code, 200)

    def test_cook_detail_view_login_required(self):
        response = self.client.get(reverse("kitchen:cook-detail", args=[1]))
        self.assertNotEqual(response.status_code, 200)


class DishTypeTestWithLoggedInUser(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="123admin123"
        )
        self.client.force_login(self.user)
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Soup")

    def test_retrieve_dish_type_list_view(self):
        response = self.client.get(DISH_TYPE_LIST_VIEW_URL)
        dishes_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishes_types_list"]),
            list(dishes_types))
        self.assertTemplateUsed(response, "kitchen/dishes_types_list.html")

    def test_create_dish_type(self):
        form_data = {
            "name": "test"
        }

        self.client.post(reverse("kitchen:dish-type-create"), data=form_data)
        new_dish_type = DishType.objects.get(name=form_data["name"])

        self.assertEqual(new_dish_type.name, form_data["name"])

    def test_dish_type_search(self):
        response = self.client.get("/dishes_types/?name=So")
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["dishes_types_list"],
            DishType.objects.filter(name__icontains="So")
        )


class DishTestWithLoggedInUser(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="123admin123"
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(name="dt")
        Dish.objects.create(
            name="New dish",
            description="excellent dish",
            price=100.00,
            dish_type=self.dish_type
        )
        Dish.objects.create(
            name="Another dish",
            description="cool dish",
            price=110.00,
            dish_type=self.dish_type
        )

    def test_retrieve_dish_list_view(self):
        response = self.client.get(DISH_LIST_VIEW_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_create_dish(self):
        form_data = {
            "name": "test",
            "description": "test dish",
            "price": 99.99,
            "dish_type": self.dish_type.id
        }
        print(form_data["dish_type"])

        self.client.post(reverse("kitchen:dish-create"), data=form_data)
        new_dish = Dish.objects.get(name=form_data["name"])

        self.assertEqual(new_dish.name, form_data["name"])

    def test_dish_search(self):
        response = self.client.get("/dishes/?name=New")
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context["dish_list"],
            Dish.objects.filter(name__icontains="New")
        )
