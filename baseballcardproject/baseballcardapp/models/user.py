from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):

    firstName = models.CharField()
    lastName = models.CharField()
    address = models.CharField()
    models.PhoneNumberField()
    email = models.EmailField()
    createdAt = models.DateTimeField()
    lastLogin = models.DateTimeField()

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})