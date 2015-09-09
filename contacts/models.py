from django.db import models
from django.utils import timezone

class Person(models.Model):
    author = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    name_in_esg = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    phone_a = models.CharField(max_length=15, blank=True, null=True)
    phone_b = models.CharField(max_length=15, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.second_name
