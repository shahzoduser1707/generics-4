from django.db import models
from datetime import datetime
# Create your models here.

class HomeModel(models.Model):
    name = models.CharField(max_length=200,default='')
    created_at = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=200,default='')
    price = models.IntegerField(default=0)
    desc = models.TextField(default="write something!")

    class Meta:
        db_table = 'HomeModel'
    def __str__(self) -> str:
        return self.name