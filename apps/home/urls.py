from django.urls import path

from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('about', AboutView.as_view()),
    path('play/<str:file>', PlayView.as_view())
]
