from django.db import models
from django.urls import reverse

class Set(models.Model):

    name = models.CharField(max_length=50)
    year = models.IntegerField()
    setnotes = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("Set")
        verbose_name_plural = ("Sets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("set_detail", kwargs={"pk": self.pk})