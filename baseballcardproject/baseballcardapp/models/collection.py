from django.db import models
from .user import User
from .card import Card

class Collection(models.Model):

    userId = models.ForeignKey(User)
    cardId = models.ForeignKey(Card)
    notes = models.CharField()

    class Meta:
        verbose_name = ("Collection")
        verbose_name_plural = ("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"pk": self.pk})