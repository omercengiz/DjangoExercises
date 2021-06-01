from django.contrib import admin
from blog.models import (CategoryModel, TextModel, CommentModel, CommunicationModel)
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


class CommunicationAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'created_date')
    search_fields = ('email',)

admin.site.register(CommunicationModel, CommunicationAdmin)

