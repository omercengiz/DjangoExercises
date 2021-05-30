from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class TextModel(models.Model):
    image = models.ImageField(upload_to='image_text')
    title = models.CharField(max_length=200)
    content = RichTextField()
    CreatedDate = models.DateTimeField(auto_now_add=True)
    editingDate = models.DateTimeField(auto_now=True)
    #SEO Url
    slug = AutoSlugField(populate_from = 'title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='text')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='texts')


    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'
        db_table = 'Text'

    def __str__(self):
        return self.title