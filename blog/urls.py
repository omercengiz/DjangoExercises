from django.urls import path,include
from blog.views import communicate, homepage

urlpatterns = [
    path('', homepage),
    path('communicate/', communicate)
]
