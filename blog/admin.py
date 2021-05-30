from django.contrib import admin
from blog.models import CategoryModel, TextModel
# Register your models here.

admin.site.register(CategoryModel)

class TextAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_display = (
        'title', 'CreatedDate', 'editingDate' 
        )


admin.site.register(TextModel, TextAdmin)