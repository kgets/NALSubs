from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='is_sub_staff')
def is_sub_staff(user):
	return user.groups.filter(name='staff').count()==1

@register.filter(name='is_sub_franchisee')
def is_sub_franchisee(user):
	return user.groups.filter(name='franchisee').count()==1