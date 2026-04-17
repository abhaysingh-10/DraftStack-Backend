from django.db import models
from django.contrib.auth.models import User  #  Django's built in User

# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # on delete is used because if user deleted then notes also gets delete
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class SubTask(models.Model):
    #one to many relationship 
    note = models.ForeignKey(Notes,on_delete=models.CASCADE,related_name='subtasks')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default= False)
    
    def __str__(self):
        return self.title
        
        