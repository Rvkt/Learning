from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

# Index Function
def index(request):
    context = {}
    return render(request, 'store/index.html', context)


# About Function
def about(request):
    return HttpResponse('About Page')


# Contact Function
def contact(request):
    return HttpResponse('Contact Page')
