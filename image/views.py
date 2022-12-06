from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Image
from .forms import *
import random

class ImageSubmitView(LoginRequiredMixin, DetailView):
    model = Image
    template_name= "random.html"

<<<<<<< HEAD
    def takeimage(request):
        if request.method =='POST':
            keg= ImageForm(request.POST, request.FILES)
            if keg.is_valid():
                keg.save()
                return redirect('home')
        else:
            keg = ImageForm()
        return render(request, 'submit.html', {'keg' : keg}) 


class ImageDetailView(LoginRequiredMixin, CreateView):
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

class CommentGet(DetailView):
    model = Image
    template_name= "random.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context    

class CommentPost(FormView,SingleObjectMixin):
    model=Image
    template_name= "random.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.image = self.object
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        image = self.get_object()
        return reverse("random", kwargs={"pk": image.pk})

# Create your views here.
=======
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
>>>>>>> ee1bfd8fa86c4311ce7f0076745979f4355e77bc
