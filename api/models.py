from django.db import models

# Create your models here.
class CyptographyTool(models.Model):
    type = models.CharField(max_length=100)
    Plaintext = models.CharField(max_length=1000)
    Ciphertext = models.CharField(max_length=1000)
    key = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.type}{self.Plaintext}{self.Ciphertext}"
    