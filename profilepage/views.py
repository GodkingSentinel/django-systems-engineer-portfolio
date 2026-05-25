from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("BAE Systems Engineer Profile")
def home(request):
    return render(request, "profilepage/home.html")