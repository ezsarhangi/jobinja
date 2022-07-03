from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from account.models import CreateProfile

# Create your views here.
def index (request):
    return render(request,"blog/index.html",{})

