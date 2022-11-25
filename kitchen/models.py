from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.years_of_experience} YOE)"

    def get_absolute_url(self) -> str:
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "dish type"
        verbose_name_plural = "dishes types"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("kitchen:dish-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.price})"
