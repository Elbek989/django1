from django.db import models


class Viloyatlar(models.Model):
    title=models.CharField(max_length=50)
    context=models.TextField(blank=True)

    def __str__(self):
        return self.title
class Tumanlar(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_at = models.IntegerField(null=True, blank=True)
    updated_at = models.IntegerField(null=True, blank=True)

    viloyat = models.ForeignKey(Viloyatlar, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Mahallalar(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_at = models.IntegerField(null=True, blank=True)
    updated_at = models.IntegerField(null=True, blank=True)
    tumanlar=models.ForeignKey(Tumanlar, on_delete=models.CASCADE)
    def __str__(self):
        return self.title




# Create your models here.
