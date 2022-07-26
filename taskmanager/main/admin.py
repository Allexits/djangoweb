from django.contrib import admin

from .models import *



class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'img', 'is_active')
    list_display_links = ('title', 'category')
    search_fields = ('title',)
    list_editable = ('is_active',)


class ShopsAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)

admin.site.register(Task)
admin.site.register(Shops, ShopsAdmin)
admin.site.register(Products, ProductsAdmin)    