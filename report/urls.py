from django.urls import path
from . import views

urlpatterns = [
    path('xlsx/', views.xlsx, name='report-xlsx'),
    path('req_summary/', views.req_summary, name='req_summary'),
    path('pdf/', views.pdf1, name='report-pdf1'),
    path('pdf1/', views.pdf, name='report-pdf'),
]
