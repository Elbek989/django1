from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=50)


    def __str__(self):
        return self.title
class Country(models.Model):
    title = models.CharField(max_length=50)
    region=models.TextField(blank=True)


    def __str__(self):
        return self.title
class Water(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.IntegerField(null=True, blank=True)
    end_date = models.IntegerField(null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# Create your models here.


# Create your models here.
