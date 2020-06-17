from django.db import models

class Set(models.Model):

    

    class Meta:
        verbose_name = ("Set")
        verbose_name_plural = ("Sets")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("set_detail", kwargs={"pk": self.pk})