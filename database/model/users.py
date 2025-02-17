from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  
    username = models.CharField(max_length=255, unique=True) 
    password = models.BinaryField() 
    refresh = models.BinaryField(default=b'auroraworld')
    createdAt = models.DateTimeField(auto_now_add=True) 
    updatedAt = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'user' 

    def __str__(self):
        return f"User(id={self.id}, username={self.username}, password={self.password}, refresh={self.refresh}, createdAt={self.createdAt}, updatedAt={self.updatedAt})"
