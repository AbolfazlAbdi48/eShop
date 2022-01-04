from django.db import models
from django.utils.html import format_html


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام دسته بندی')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{self.id}/{self.name.replace(" ", "-")}'


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to='products/images/', verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت محصول (تومان)')
    sale_count = models.IntegerField(default=0, verbose_name='تعداد فروش')
    product_count = models.IntegerField(verbose_name='تعداد محصول')
    categories = models.ManyToManyField(Category, related_name='categories', verbose_name='دسته بندی ها')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین تغییر')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'{self.id}/{self.title.replace(" ", "-")}'

    def thumbnail_tag(self):
        return format_html(f'<img width=120 height=75 style="border-radius: 8px" src="{self.image.url}">')

    def price_tag(self):
        return f'{self.price} تومان'

    thumbnail_tag.short_description = "تصویر محصول"
    price_tag.short_description = "قیمت محصول (تومان)"
