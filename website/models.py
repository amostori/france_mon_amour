from django.db import models

class Post(models.Model):
    body = models.TextField()
    manage = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.body
    
