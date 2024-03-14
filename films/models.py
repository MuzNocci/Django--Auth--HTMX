from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class FilmReview(models.Model):


    class Status(models.IntegerChoices):

        DRAFT = (1, 'Draft')
        PUBLISHED = (2, 'Published')


    class Rating(models.IntegerChoices):

        BAD = (1, 'Bad')
        POOR = (2, 'Poor')
        FAIR = (3, 'Fair')
        GOOD = (4, 'Good')
        EXCELLENT = (5, 'Excellent')
        EXCEPTIONAL = (6, 'Exceptional')


    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=250, blank=False, null=False)
    status = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    body = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices, default=Rating.GOOD)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    def __str__(self):

        return f'{self.title} ({self.status})'