from django.db import models

class Card(models.Model):

    

    class Meta:
        verbose_name = ("Card")
        verbose_name_plural = ("Cards")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("card_detail", kwargs={"pk": self.pk})
