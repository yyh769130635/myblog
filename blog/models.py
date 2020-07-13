from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default="title")
    context = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        """返回一个对象的描述信息"""
        return self.title
