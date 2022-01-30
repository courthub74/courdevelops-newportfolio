from os import name
from django.urls import path
from . import views

app_name = "portfolioapp"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContatctView.as_view(), name="contact"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]