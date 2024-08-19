from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request): 
  return render(request, "pages/index.html", {
    'active_menu': "home"
  })

def aboutUs(request): 
  return render(request, "pages/about-us.html", {
    'active_menu': "about-us"
  })

def webClient(request): 
  return render(request, "pages/web-client.html", {
    'active_menu': "web-client"
  })

def mobile(request): 
  return render(request, "pages/mobile.html", {
    'active_menu': "mobile"
  })

def pricing(request): 
  return render(request, "pages/pricing.html", {
    'active_menu': "pricing"
  })