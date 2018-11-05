from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	# /home/
	path('', views.index, name='index'),
	path('index/', views.index, name ='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('franchisee/', views.franchisee, name='franchisee'),
	path('staff/', views.staff, name='staff'),
]