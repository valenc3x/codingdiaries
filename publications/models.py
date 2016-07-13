from django.db import models

from users.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(blank=True, max_length=140)
    owner = models.ForeignKey(User, related_name='projects')
    description = models.CharField(blank=True, max_length=255)
    followers = models.ManyToManyField(User, related_name='following')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s by %s" % (self.name, self.owner)

class Publication(models.Model):
    title = models.CharField(blank=True, max_length=140)
    text = models.TextField(blank=True)
    project = models.ForeignKey(Project, related_name='publications')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return "%s in %s" % (self.title, self.project)
