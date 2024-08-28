from django.db import models

class Cars(models.Model):
    model = models.CharField(max_length=200)
    engine = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image_url = models.JSONField(default=list, blank=False)
    colors = models.JSONField(default=list, blank=False) 
    versions = models.JSONField(default=list, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)