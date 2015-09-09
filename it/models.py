from django.db import models
from django.utils import timezone

class Language(models.Model):
    author = models.ForeignKey('auth.User')
    language =models.CharField(max_length=200, primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.language

class Topic(models.Model):
    author = models.ForeignKey('auth.User')
    topic =models.CharField(max_length=200, primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.topic

class Itmanual(models.Model):
    author = models.ForeignKey('auth.User')
    language =models.ForeignKey(Language)
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        temp = str(self.language) + ' ' + str(self.topic)
        return temp
