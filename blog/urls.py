from django.urls import path
from .views import home, PortfolioView


urlpatterns = [
    path('', home, name='blog-home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('contact/', contact, name='contact')
]
