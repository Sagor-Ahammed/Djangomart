from django.contrib import admin

# Register your models here.

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('slug','category_name')

admin.site.register(Category,CategoryAdmin)