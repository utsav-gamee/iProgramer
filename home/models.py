


from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    #image = models.ImageField(upload_to='static/img', default="")
    
    def __str__(self):
        return "Message from " + self.name 