from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .decorators import franchisee_required, staff_required


def index(request):
	return render(request, 'public/index.html', {})

def about(request):
	return render(request, 'public/about.html', {})

def contact(request):
	return render(request, 'public/contact.html', {})

@login_required
@staff_required
def staff(request):
	auth_files = Upload.objects.filter(vis_staff=True).order_by('-upload_date')
	return render(request, 'public/staff.html', auth_files)

@login_required
@franchisee_required
def franchisee(request):
	auth_files = Upload.objects.filter(vis_franchisee=True).order_by('-upload_date')
	return render(request, 'public/franchisee.html', auth_files)

