from django.db import models

class Movies(models.Model):
    title = models.CharField('Name', max_length=100)
    category = models.CharField('Category', max_length=100)
    rate = models.CharField('Rating', max_length=10)
    image = models.ImageField('Poster', upload_to='images/')
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'