from django.urls import reverse
from django.db import models

class Task(models.Model):
    title = models.CharField('Name',max_length=50)
    desc = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'Task Category'
        verbose_name_plural= 'Task Categories'

class Shops(models.Model):
    title = models.CharField(max_length=50,verbose_name='name')
    desc = models.TextField(blank=True,verbose_name='description')
    img = models.ImageField(upload_to='main/images/shops',default=False,verbose_name='image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop', kwargs={'id':self.pk})

    class Meta:
        verbose_name= 'Shop'
        verbose_name_plural= 'Shops'
        ordering = ['title']


class Products(models.Model):
    title = models.CharField(max_length=50,verbose_name='name')
    desc = models.TextField(blank=True,verbose_name='description')
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='main/images',default=False,verbose_name='image')
    category = models.ForeignKey(Shops,on_delete=models.CASCADE,default=1,verbose_name='shop')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name= 'Product'
        verbose_name_plural= 'Products'
        ordering = ['category','title']