"""medlink URL Configuration

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
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from client.views import *
from libs.views import *
from dashboard.views import accounts_profile

from crud_ajax.views import CreateCrudUser, CrudView, DeleteCrudUser, UpdateCrudUser
from frontend.views import *
from crud_ajax.models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'joins/', include('joins.urls')),
    url(r'libs/', include('libs.urls')),
    url(r'client/', include('client.urls')),
    url(r'snippets/', include('snippets.urls')),
    url(r'dashboard/', include('dashboard.urls')),
    url(r'frontend/', include('frontend.urls')),

    url(r'^', include('allauth.urls')),
    url(r'^accounts/profile/', accounts_profile, name='accounts-profile'),
    
    url(r'^client/', client, name='client'),
    url(r'^client-detail/(?P<id>.*)$', client_detail, name='client-detail'),

    # url(r'^crud/', CrudView.as_view(), name='crud_ajax'),
    
    
    path('crud_ajax/', CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)