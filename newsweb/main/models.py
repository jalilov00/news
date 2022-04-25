from django.db import models


class New(models.Model):
    img = models.ImageField(upload_to='media/news', blank = True, null = True)
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name

