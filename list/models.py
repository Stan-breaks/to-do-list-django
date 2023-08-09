from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_lists")
    text=models.CharField(max_length=200)
    done=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now_add=True)