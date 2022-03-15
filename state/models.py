from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    location_name = models.CharField(default='Location Name', max_length=100, unique= True)
    slug = models.SlugField(max_length=100, unique=True)
    state = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('state_by_category', args = [self.slug])

    def __str__(self):
        return self.state_name
