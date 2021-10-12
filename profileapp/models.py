from django.contrib.auth.models import User
from django.db import models


LANGUAGE_CHOICES = (('English', 'English'), ('Japanese', 'Japanese'), ('chinese', 'chinese'),
                    ('vietnamese', 'vietnamese'), ('Indonesia', 'Indonesia'), ('arabic', 'arabic'),
                    ('Bengal', 'Bengal'), ('german', 'german'), ('spanish', 'spanish'), ('french', 'french'),
                    ('Hindi', 'Hindi'), ('italian', 'italian'), ('malaysian', 'malaysian'), ('dutch', 'dutch'),
                    ('portukal ', 'portukal '), ('russian', 'russian'), ('thai', 'thai'), ('turkish', 'turkish'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, null=False, blank=False)
