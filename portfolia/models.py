from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name