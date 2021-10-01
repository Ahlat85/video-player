from django.shortcuts import render

from django.views.generic import TemplateView, ListView, FormView

from .models import *

import website

video = VideoModel()

class IndexView(TemplateView):
  template_name = 'home/index.html'
  
  def get_context_data(self, **kwargs):
    context = {}
    context['title_page'] = 'Video Player'
    context['videos'] = video.fetch_all()
    return context 
    
class AboutView(TemplateView):
  template_name = 'home/about.html'
  
  def get_context_data(self, **kwargs):
    context = {}
    context['title_page'] = 'About'
    return context 
  
class TutorialView(TemplateView):
  template_name = 'home/tutorial.html'
  
class PlayView(TemplateView):
  template_name = 'home/play.html'
  
  def get_context_data(self, **kwargs):
    context = {}
    context['title_page'] = kwargs['file'][:-4]
    context['video'] = video.fetch(kwargs['file'])
    return context 