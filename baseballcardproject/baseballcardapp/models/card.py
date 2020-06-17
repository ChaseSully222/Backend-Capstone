from django.db import models
from django.urls import reverse
from .player import Player
from .set import Set

class Card(models.Model):

    playerId = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    year = models.IntegerField()
    setId = models.ForeignKey(Set, on_delete=models.DO_NOTHING)
    cardNumber = models.CharField(max_length=50)
    attribute = models.CharField(max_length=50, null=True)
    imagePathFront = models.CharField(max_length=50, null=True)
    imagePathBack = models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name = ("Card")
        verbose_name_plural = ("Cards")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("card_detail", kwargs={"pk": self.pk})
