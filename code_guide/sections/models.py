# sections/models.py
from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class SubSection(models.Model):
    section = models.ForeignKey(Section, related_name="subsections", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
