from django.db import models

class blog(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=555)