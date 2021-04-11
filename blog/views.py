from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Project



def home(request):
    return render(request, 'blog/home.html')


class PortfolioView(ListView):
    template_name = 'blog/portfolio.html'
    queryset = Project.objects.all()
    context_object_name = 'projects'


def contact(request):
    return render(request, 'blog/contact.html')
