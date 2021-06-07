
from django.shortcuts import render


def homepage(request):
    context = {
        'name' : 'omercengiz607@gmail.com'
    }
    return render(request, 'pages/homepage.html', context=context) 