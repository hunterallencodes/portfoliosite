from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    page_url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio_photos', blank=True, null=True)

    def __str__(self):
        return self.title
