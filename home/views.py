from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# About Page View
def myPortfolio(request):
    return render(request, 'my-portfolio.html')

# Home Page View
def homePage(request):
    return HttpResponse('This is my home page')

# Contact Page View
def contactPage(request):
    return HttpResponse('Contact us at: contact@example.com')

# Services Page View
def servicesPage(request):
    return HttpResponse('These are our services')