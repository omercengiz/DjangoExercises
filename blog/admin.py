from django.contrib import admin
from blog.models import (CategoryModel, TextModel, CommentModel)
# Register your models here.

admin.site.register(CategoryModel)

class TextAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = (
        'title', 'created_date', 'editing_date' 
        )


admin.site.register(TextModel, TextAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author_person', 'text', 'created_date', 'editing_date'
    )
    search_fields = ('author_person__username',)

admin.site.register(CommentModel, CommentAdmin)
