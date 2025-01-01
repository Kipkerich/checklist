from django.contrib import admin
from .models import UserProfile, Category, ChecklistItem

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(ChecklistItem)
