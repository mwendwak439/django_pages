from django.db import models

class Greeting(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']   # newest first

    def __str__(self):
        return f'{self.name}: {self.message[:30]}:{self.email}'