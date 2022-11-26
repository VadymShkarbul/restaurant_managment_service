from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Cook, DishType, Dish


class TestStringMethods(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="Food"
        )
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="1a2T3e4u6v0",
            first_name="Test",
            last_name="Tester",
            years_of_experience=2
        )
        self.dish = Dish.objects.create(
            name="New dish",
            description="excellent dish",
            price=100.00,
            dish_type=self.dish_type
        )

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), f"{self.dish_type.name}")

    def test_cook_str(self):
        self.assertEqual(str(self.user),
                         f"{self.user.first_name} "
                         f"{self.user.last_name} "
                         f"({self.user.years_of_experience} YOE)")

    def test_dish_str(self):
        self.assertEqual(str(self.dish), f"{self.dish.name} "
                                         f"({self.dish.price})")

    def test_create_cook_with_yoe(self):
        self.assertEqual(self.user.years_of_experience, 2)

    def test_dish_type_verbose_name_plural(self):
        self.assertEqual(
            self.dish_type._meta.verbose_name_plural,
            "dishes types"
        )

    def test_dish_verbose_name_plural(self):
        self.assertEqual(
            self.dish._meta.verbose_name_plural,
            "dishes"
        )

    def test_if_users_ordered_by_username(self):
        Cook.objects.create(
            username="Cook",
            password="123cook123",
            years_of_experience=1
        )
        self.assertEqual(Cook.objects.first().username, "Cook")

    def test_if_dish_type_ordered_by_name(self):
        DishType.objects.create(
            name="Almond"
        )
        self.assertEqual(DishType.objects.first().name, "Almond")
