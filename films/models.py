from django.db import models



class Film(models.Model):

    title = models.CharField(max_length=250, blank=False, null=False)


    def __str__(self):

        return self.title