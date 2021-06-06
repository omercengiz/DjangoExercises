from django.db import models
from django.contrib.auth.models import User
from blog.models import TextModel
from blog.abstract_models import DataAbstractModel

class CommentModel(DataAbstractModel):
    author_person = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    text = models.ForeignKey(TextModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()


    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural= 'Comments'


    def __str__(self):
        return self.author_person.username