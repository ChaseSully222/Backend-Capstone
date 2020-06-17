from django.db import models

class Player(models.Model):

    firstName = models.CharField()
    lastName = models.CharField()

    class Meta:
        verbose_name = ("Player")
        verbose_name_plural = ("Players")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("player_detail", kwargs={"pk": self.pk})