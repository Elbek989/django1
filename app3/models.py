
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title




# Create your models here.
