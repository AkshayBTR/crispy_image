from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    top_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,primary_key=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name