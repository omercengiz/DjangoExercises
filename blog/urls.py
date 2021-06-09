from django.urls import path,include
from blog.views import communicate, homepage, category_func, maps_func

urlpatterns = [
    path('', homepage, name='homepage'),
    path('communicate/', communicate, name='communicate'),
    path('category/<slug:categorySlug>', category_func, name='category'),
    path("api/v1/maps", maps_func, name="maps")
]
