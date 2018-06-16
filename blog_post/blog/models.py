from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	name = models.CharField(max_length=80)
	description = models.TextField()
	date = models.DateTimeField()
	image = models.FileField(null=True, blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
