from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  
    username = models.CharField(max_length=255) 
    password = models.CharField(max_length=255)  
    salt = models.CharField(max_length=255)  
    createdAt = models.DateTimeField(auto_now_add=True) 
    updatedAt = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'user' 

    def __str__(self):
        return self.username
