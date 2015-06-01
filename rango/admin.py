from django.contrib import admin
from rango.models import Category, Page
# Register your models here.

    list_display = ['title', 'category', 'url']


admin.site.register(Category)
admin.site.register(Page, PageAdmin)