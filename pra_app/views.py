from django.shortcuts import render
from django.http import HttpResponse

def hellofunction(request):
    return render(request,'example/example.html')
# Create your views here.
