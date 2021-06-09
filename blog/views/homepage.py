
from django.shortcuts import render
from blog.models import TextModel
from django.core.paginator import Paginator

def homepage(request):
    texts = TextModel.objects.order_by('-id')
    page = request.GET.get('page')

    paginator = Paginator(texts, 2) 
    
    
    return render(request, 'pages/homepage.html', context={
        'texts':paginator.get_page(page)
        }) 