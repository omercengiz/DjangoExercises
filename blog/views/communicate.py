from django.shortcuts import render


def communicate(request):
    context = {
        'name' : 'omercengiz607@gmail.com'
    }
    return render(request, 'pages/communicate.html', context={}) 