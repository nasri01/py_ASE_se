from django.urls import path
from . import views

urlpatterns = [
    path('xlsx/', views.xlsx, name='report-xlsx'),
    path('pdf1/', views.pdf, name='report-pdf'),
    path('pdf/', views.pdf1, name='report-pdf1'),
]
