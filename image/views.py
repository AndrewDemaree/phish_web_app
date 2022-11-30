from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from .forms import *
import random


def takeimage(request):
    if request.method =='POST':
        keg= ImageForm(request.POST, request.FILES)
        if keg.is_valid():
            keg.save()
            return redirect('home')
    else:
        keg = ImageForm()
    return render(request, 'submit.html', {'keg' : keg}) 
       
def showimage(request):   
    if request.method == 'GET':
        t= Image.objects.last()
        num = t.id
        tootles  = random.randint(0,num)
        displayimage= Image.objects.get(id=tootles)
        imagefile= displayimage.imagefile
        return render((request, 'home.html', imagefile))    

# Create your views here.
