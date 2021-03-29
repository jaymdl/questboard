from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Questboard(models.Model):
	name = models.CharField(max_length=50, blank=False)
	description = models.CharField(max_length=150, blank=False)
	required_stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
	creator = models.ForeignKey(User, on_delete=models.CASCADE)