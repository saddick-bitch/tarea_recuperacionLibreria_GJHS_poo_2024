from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField('ISBN', max_length=13, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})