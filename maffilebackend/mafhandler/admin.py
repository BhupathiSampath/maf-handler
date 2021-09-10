from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mafhandler.models import MafFile
# Register your models here.

admin.site.register(MafFile)