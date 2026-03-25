from django.contrib.auth.models import User
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    manufacturing_since = models.IntegerField()
    logo = models.ImageField(upload_to='brands/',blank=True, null=True)

    def __str__(self):
        return self.name

class MobileModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=100) # 例如 iOS, Android
    photo = models.ImageField(upload_to='phones/',blank=True, null=True)

    def __str__(self):
        return self.model_name

class Review(models.Model):
    # 新增这一行，建立与用户的关联
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    models_covered = models.ManyToManyField('MobileModel')

    def __str__(self):
        return self.title