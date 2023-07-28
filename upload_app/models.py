from django.db import models

# Create your models here.

class Uploads(models.Model):
	image = models.ImageField(upload_to="images")
	desc = models.CharField(max_length=100)

	def __str__(self):
		return self.desc[0:40]


class UploadFile(models.Model):
	file = models.FileField(upload_to="files")
	desc = models.CharField(max_length=100)

	def __str__(self):
		return self.desc[0:40]