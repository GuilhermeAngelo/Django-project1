from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html')


def about(request):
    return HttpResponse('About page')


def contact(request):
    return HttpResponse("Contact's page")

