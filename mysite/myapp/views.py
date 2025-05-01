# my_simple_app/views.py

from django.shortcuts import render

def simple_view(request):
    context = {'message': 'Hello, Django with CSS!'}
    return render(request, 'myapp/index.html', context)