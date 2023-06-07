from django.db import models

# Create your models here.


class Input(models.Model):
    photo = models.ImageField('Фото', default='None', upload_to='photos')

