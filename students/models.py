from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    year_level = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['year_level']