from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
	return render(request, 'public/home.html', {})


def about(request):
	return render(request, 'public/about.html', {})

def contact(request):
	return render(request, 'public/contact.html', {})