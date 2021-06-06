from django.contrib import admin
from blog.models import (CategoryModel, TextModel, CommentModel, CommunicationModel)
# Register your models here.

admin.site.register(CategoryModel)

@admin.register(TextModel)
class TextAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = (
        'title', 'created_date', 'editing_date' 
        )

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author_person', 'text', 'created_date', 'editing_date'
    )
    search_fields = ('author_person__username',)



@admin.register(CommunicationModel)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'created_date')
    search_fields = ('email',)



