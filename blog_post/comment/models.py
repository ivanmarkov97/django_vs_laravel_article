from django.db import models
from blog.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
	text = models.TextField()
	likes = models.PositiveIntegerField()
	date = models.DateTimeField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.text
