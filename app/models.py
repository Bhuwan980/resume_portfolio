from django.db import models

# Create your models here.
class Contact(models.Model):
	FirstName=models.CharField(max_length=20)
	LastName = models.CharField(max_length=15)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.FirstName