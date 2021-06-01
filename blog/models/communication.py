from django.db import models


class CommunicationModel(models.Model):
    email = models.EmailField(max_length=254)
    name_surname = models.CharField(max_length=160)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'communication'
        verbose_name = 'Communication'
        verbose_name_plural = 'Communication'
        

    def __str__(self):
        return self.email