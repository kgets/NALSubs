from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .decorators import franchisee_required, staff_required
from .models import Upload
import os
from django.conf import settings


def index(request):
	# images = os.listdir(os.path.join(settings.STATIC_ROOT, 'images/stores'))
	return render(request, 'public/index.html', {}) #'img': images

def about(request):
	return render(request, 'public/about.html', {})

def contact(request):
	return render(request, 'public/contact.html', {})

@login_required
@staff_required
def staff(request):
	auth_files = {'queryset':Upload.objects.filter(vis_staff=True).order_by('-upload_date')}
	return render(request, 'public/staff.html', auth_files)

@login_required
@franchisee_required
def franchisee(request):
	auth_files = {'queryset':Upload.objects.filter(vis_franchisee=True).order_by('-upload_date')}
	return render(request, 'public/franchisee.html', auth_files)

