from django.contrib import admin

from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'img', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    prepopulated_fields = {'slug':('title',)}


class ShopsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'img', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Menu, MenuAdmin)  
admin.site.register(Shops, ShopsAdmin)
admin.site.register(Products, ProductsAdmin)    