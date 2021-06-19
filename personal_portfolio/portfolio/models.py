from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')  # pip install Pillow always needed for image
    url = models.URLField(blank=True)  # blank=True means the field can be null

    def __str__(self):
        return self.title