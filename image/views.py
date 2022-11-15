from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
from .forms import *
import random


def showimage(request):
    t= Image.objects.last()
    num = t.id
    tootles  = random.randint(0,num)
    displayimage= Image.objects.get(id=tootles)

    imagefile= displayimage.imagefile
    if request.method == 'GET':
            return render((request, 'html', imagefile))
    if request.method =='POST':
        form= ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, '.html', {'form' : form})    
    
    
def success(request):  
    return HttpResponse('successfully uploaded')

# Create your views here.
