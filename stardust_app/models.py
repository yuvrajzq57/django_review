from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=100)
    email = models.EmailField(max_length=12)
    phone = models.CharField(max_length=10)
    feedback = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.usn}"