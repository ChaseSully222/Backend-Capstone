from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .card import Card

class Collection(models.Model):

    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cardId = models.ForeignKey(Card, on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("Collection")
        verbose_name_plural = ("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"pk": self.pk})




