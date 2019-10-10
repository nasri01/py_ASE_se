from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.login,name='login1'),
    path('log_out/', views.logout,name='logout1'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('req_list/', views.req_list,name='req_list'),
    path('recal_list/', views.recal_list,name='recal_list'),
    path('report_list/', views.report_list,name='report_list'),
    path('edit/', views.edit_report,name='edit_report'),
    path('recal/', views.recal_report,name='recal_report'),
    path('change_email/', views.change_email,name='change_email'),

]
