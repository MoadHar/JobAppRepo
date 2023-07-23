## commands
#makemigrations: for creating new migrations based on changes in the models
#sqlmigrate: displays sql statements for migration
#migrate: running migration
#shomigrations: lists migrations of the projects along with there status

from django.db import models

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()

    def __str__(self):
    	return self.title

class Person(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	birthyear = models.IntegerField()
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=50)

	def __str__(self):
		return self.firstname + ' ' + self.lastname + ' (from) ' + self.city

