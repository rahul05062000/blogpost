from django.db import models
from django.contrib.auth.models import AbstractUser



class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_at = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Untitled Post"





class Comment(models.Model):
    post_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(max_length=255)

    def __str__(self):
        return self.content
    

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} {self.lastname}"
    
    @classmethod
    def create_from_list(cls, data_list):
        if len(data_list) != 4:
            raise ValueError("Data list must contain exactly four elements")

        name, lastname, email, password = data_list
        return cls.objects.create(name=name, lastname=lastname, email=email, password=password)
    






