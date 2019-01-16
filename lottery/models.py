from django.db import models

# Create your models here.
class Suffix(models.Model):
        def __str__(self):
                return self.name
        name = models.CharField(max_length=100)
        needs_s = models.BooleanField(default=0)

class MiddleTerm(models.Model):
        def __str__(self):
                return self.name
        name = models.CharField(max_length=100)
        is_own_word = models.BooleanField(default=0)

class Prefix(models.Model):
        def __str__(self):
                return self.name
        name = models.CharField(max_length=100)

class Course(models.Model):
        def __str__(self):
                return self.name
        name = models.CharField(max_length=300)

