from django.core.validators import MaxLengthValidator
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(
        validators=[MaxLengthValidator(2000)],
        blank=True, null=True
    )
    email = models.EmailField(max_length=250)
    jabber = models.EmailField(max_length=250)
    skype = models.CharField(max_length=60, blank=True, null=True)
    other = models.TextField(
        validators=[MaxLengthValidator(2000)],
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Request(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
