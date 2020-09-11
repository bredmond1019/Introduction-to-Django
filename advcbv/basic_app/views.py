from django.shortcuts import render
from django.views.generic import (TemplateView, View, 
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from . import models
from django.urls import reverse_lazy
class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION'
    #     return context



class SchoolListView(ListView):
    model = models.School
    # this returns a list called school_list
    
    # or you can change the name of the list like this
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    #this only returns school  (in lower case), but we can change it like below:
    context_object_name = 'school_detail'
    
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')

    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")