from django.test import TestCase

from kitchen.forms import CookCreationForm, CookYOEUpdateForm


class CookFormsTest(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            "username": "test",
            "password1": "123test123",
            "password2": "123test123",
            "first_name": "first",
            "last_name": "last",
        }

    def test_cook_creation_form_is_valid_with_added_fields(self):
        self.form_data.update({"years_of_experience": 3})

        form = CookCreationForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.form_data)

    def test_years_of_experience_validation(self):
        incorrect_yoe = [-1, 51]

        for i_yeo in incorrect_yoe:
            with self.subTest(amount=i_yeo):
                self.form_data.update({"years_of_experience": i_yeo})

                form = CookYOEUpdateForm(data=self.form_data)

                self.assertFalse(form.is_valid())
