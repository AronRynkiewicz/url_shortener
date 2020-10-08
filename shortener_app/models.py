from django.db import models


class URL(models.Model):
    user_url = models.CharField(max_length=150)
    shortened_url = models.CharField(max_length=8)
    created_date = models.DateTimeField(auto_now_add=True)
