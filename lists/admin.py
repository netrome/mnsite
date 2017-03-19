from django.contrib import admin
from .models import MnList, MnItem, Profile

# Register your models here.

admin.site.register(MnList)
admin.site.register(MnItem)
admin.site.register(Profile)
