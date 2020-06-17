from django.db import models

class User(models.Model):

    

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})