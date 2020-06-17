from django.db import models

class Set(models.Model):

    name = models.CharField()
    year = models.IntegerField(max_length=4)
    notes = models.CharField()

    class Meta:
        verbose_name = ("Set")
        verbose_name_plural = ("Sets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("set_detail", kwargs={"pk": self.pk})