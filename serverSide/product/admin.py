from django.contrib import admin

from .models import Category, Product, Mark

admin.site.register(Category)
admin.site.register(Mark)
admin.site.register(Product)
