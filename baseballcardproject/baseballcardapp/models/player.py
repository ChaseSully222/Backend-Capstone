from django.db import models
from django.urls import reverse

class Player(models.Model):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Player")
        verbose_name_plural = ("Players")

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def get_absolute_url(self):
        return reverse("player_details", kwargs={"pk": self.pk})