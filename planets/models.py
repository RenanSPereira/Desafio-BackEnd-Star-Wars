from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False)
    climate = models.TextField(max_length=20, null=False, blank=False)
    terrain = models.TextField(max_length=20, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)    
    films_qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name