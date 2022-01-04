from django.db import models


# Create your models here.
class Customer(models.Model):
    email = models.EmailField(unique=True, verbose_name='ایمیل مشتری')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def __str__(self):
        return self.email
