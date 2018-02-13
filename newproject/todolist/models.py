from django.db import models
from django.utils import timezone

class Category(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Todo(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
