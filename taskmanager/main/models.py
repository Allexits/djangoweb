from django.urls import reverse
from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=50,verbose_name='name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    desc = models.TextField(blank=True,verbose_name='description')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name= 'Menu'
        verbose_name_plural= 'Menus'
        ordering = ['pk']


class Shops(models.Model):
    title = models.CharField(max_length=255,verbose_name='name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    desc = models.TextField(blank=True, verbose_name='description')
    img = models.ImageField(upload_to='main/images/shops', verbose_name='image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop', kwargs={'page_slug':self.slug})

    class Meta:
        verbose_name= 'Shop'
        verbose_name_plural= 'Shops'
        ordering = ['title']


class Products(models.Model):
    title = models.CharField(max_length=50,verbose_name='name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    desc = models.TextField(blank=True,verbose_name='description')
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='main/images',verbose_name='image')
    category = models.ForeignKey(Shops,on_delete=models.DO_NOTHING,default=1,verbose_name='shop')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= 'Product'
        verbose_name_plural= 'Products'
        ordering = ['category','title']