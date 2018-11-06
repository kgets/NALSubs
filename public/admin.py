from django.contrib import admin
from .models import Upload #, authType
from django.contrib.auth.admin import UserAdmin

admin.site.register(Upload)
# admin.site.register(authType)