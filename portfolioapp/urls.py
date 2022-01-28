from django.urls import path
from . import views

app_name = "portfolioapp"

urlpatterns = [
    path(' ', views.home, name='home'),
]