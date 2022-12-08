from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Image
from .forms import *
import random

class ImageSubmitView(LoginRequiredMixin, DetailView):
    model = Image
    template_name= "random.html"

    def takeimage(request):
        if request.method =='POST':
            keg= ImageForm(request.POST, request.FILES)
            if keg.is_valid():
                keg.save()
                return redirect('home')
        else:
            keg = ImageForm()
        return render(request, 'submit.html', {'keg' : keg}) 


class ImageDetailView(LoginRequiredMixin, DetailView):
    model = Image
    template_name= "submit.html"
    def showimage(request):   
        if request.method == 'GET':
            t= Image.objects.last()
            num = t.id
            tootles  = random.randint(0,num)
            displayimage= Image.objects.get(id=tootles)
            imagefile= displayimage.imagefile
            return render((request, 'home.html', imagefile))

class CommentGet(ListView):
    model = Comment
    template_name= "Comment.html"

class CommentUpdateView(UpdateView):
    model = Comment
    form_class= CommentForm
    template_name= "Comment_edit.html"


class CommentDetailView(DetailView):
    model= Comment
    template_name="Chat_detail.html"

class CommentCreateView(CreateView,SingleObjectMixin):
    model=Comment
    form_class= CommentForm
    template_name= "Chat_create.html"

class CommentDeleteView(DeleteView, SingleObjectMixin):
    model=Comment
    template_name= 'Chat_delete.html'
    success_url = reverse_lazy("comment")
    
# Create your views here.
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
