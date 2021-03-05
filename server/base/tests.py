# from django.test import TestCase
#
# # Create your tests here.
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from .views import MainTemplateView

print(MainTemplateView.__dict__)
