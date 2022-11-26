from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="1a2S3r4s5t"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username="cook",
            password="123cook123",
            years_of_experience=1
        )

    def test_cook_yoe_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.years_of_experience)

    def test_cook_yoe_in_additional(self):
        url = reverse("admin:kitchen_cook_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertContains(response, self.user.years_of_experience)

    def test_dish_in_admin(self):
        url = reverse("admin:kitchen_dish_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
