from django.db import models
from django.views.generic.edit import CreateView

# Create your models here.
class Category(models.Model):
    class Meta:
            verbose_name_plural = 'categories'
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
