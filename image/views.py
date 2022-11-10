from django.shortcuts import render
from .models import Image
from .forms import ImageForm
import random


def showimage(request):
    t= Image.objects.last()
    num = t.id
    tootles  = random.randint(0,num)
    lastimage= Image.objects.get(id=tootles)

    imagefile= lastimage.imagefile


    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'imagefile': imagefile
              }
    
      
    return render(request, 'home.html', context)

# Create your views here.
