from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # optional
    updated_at = models.DateTimeField(auto_now=True)      # optional

    def __str__(self):
        return f"{self.name} - {self.email}"
