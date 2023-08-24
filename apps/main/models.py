from django.db import models

# Create your models here.

class Reclama(models.Model):
    text = models.CharField(
        verbose_name='текст рекламы',
        max_length=200
    )
    img = models.ImageField(
        verbose_name='картинка рекламы',
        upload_to='reclama/',
        default='reclama/img.png',
        null=True,
        blank=True
    )