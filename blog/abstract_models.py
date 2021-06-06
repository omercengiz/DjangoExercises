from django.db import models


class DataAbstractModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    editing_date = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True