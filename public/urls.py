from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
	# /home/
	path('', views.index, name='index'),
	path('index/', views.index, name ='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('franchisee/', views.franchisee, name='franchisee'),
	path('staff/', views.staff, name='staff'),
    re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)