"""ww URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import acc.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', include('acc.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', acc.views.submit,name='dashboard'),
    path('report/', include('report.urls')),
    path('form/', include('form.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'acc.views.my_custom_page_not_found_view'
handler500 = 'acc.views.my_custom_error_view'
handler403 = 'acc.views.my_custom_permission_denied_view'
handler400 = 'acc.views.my_custom_bad_request_view'