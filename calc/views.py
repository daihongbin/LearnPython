from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,'home.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

# /add/3/4
def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request,a,b):
    print(123)
    return HttpResponseRedirect(
        reverse('add2',args=(a,b))
    )