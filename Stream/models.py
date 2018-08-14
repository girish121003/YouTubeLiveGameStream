from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    id=models.AutoField(primary_key=True)
    UserId=models.CharField(max_length=40)
    DisplayMessage=models.CharField(max_length=1000)
    def __str__(self):
        return self.DisplayMessage
    class Meta:
        managed = True

