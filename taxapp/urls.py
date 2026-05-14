from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('taxrate/', views.show_tax_rate),
    path('<int:number>/', views.calculate_tax),
]