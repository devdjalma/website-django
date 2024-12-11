from django.contrib import admin
from .models import UserData
from .models import UserCategory

# Register your models here.
admin.site.register(UserCategory)
admin.site.register(UserData)

