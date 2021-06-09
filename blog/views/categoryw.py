from django.shortcuts import render, get_object_or_404
from blog.models import TextModel, CategoryModel
from django.core.paginator import Paginator


def category_func(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug = categorySlug)
    texts = category.text.all()
    print(texts)

    page = request.GET.get('page')

    paginator = Paginator(texts, 2) 
    
    
    return render(request, 'pages/homepage.html', context={
        'texts':paginator.get_page(page)
        }) 