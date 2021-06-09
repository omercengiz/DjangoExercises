from django.shortcuts import render


def communicate(request):
    context = {
        'key' : 'title content hi'
    }
    return render(request, 'pages/communicate.html', context=context) 