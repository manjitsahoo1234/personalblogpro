from django.db import models

# Create your models here.
class Category(models.Model):
    cid= models.AutoField(primary_key=True)
    title= models.CharField(max_length=150)
    description= models.TextField()
    url= models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    pid= models.AutoField(primary_key=True)
    title= models.CharField(max_length=150)
    description= models.TextField()
    url= models.CharField(max_length=100)
    cat=models.ForeignKey(Category, on_delete= models.CASCADE)


    def __str__(self):
        return self.title
