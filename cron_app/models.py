from django.db import models


class RandomText(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    random_text = models.TextField()
