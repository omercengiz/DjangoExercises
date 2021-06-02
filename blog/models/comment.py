from django.db import models
from django.contrib.auth.models import User
from blog.models import TextModel

class CommentModel(models.Model):
    author_person = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    text = models.ForeignKey(TextModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    editing_date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural= 'Comments'


    def __str__(self):
        return self.author_person.username