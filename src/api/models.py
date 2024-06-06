from django.db import models

# Create your models here.
# class Category(models.Model):
#     name=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    category=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title