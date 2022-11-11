from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookYOEUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = [
            "first_name",
            "last_name",
            "years_of_experience",
        ]

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(
        years_of_experience,
):
    if years_of_experience < 0:
        raise ValidationError("Not negative values!")
    if years_of_experience > 50:
        raise ValidationError("Are you sure?")

    return years_of_experience


class DishUpdateForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

    def clean_price(self):
        return validate_price(self.cleaned_data["price"])


def validate_price(
        price,
):
    if price < 0:
        raise ValidationError("Not negative values!")

    return price
