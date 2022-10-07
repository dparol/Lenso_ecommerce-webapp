from unicodedata import category
from django.contrib import admin
from .models import Category
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display= ('category_name','slug')

admin.site.register(Category,categoryadmin)
