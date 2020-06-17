from django.db import models

class Collection(models.Model):

    

    class Meta:
        verbose_name = ("Collection")
        verbose_name_plural = ("Collections")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"pk": self.pk})