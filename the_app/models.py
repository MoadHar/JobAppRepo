## commands
#makemigrations: for creating new migrations based on changes in the models
#sqlmigrate: displays sql statements for migration
#migrate: running migration
#shomigrations: lists migrations of the projects along with there status

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Skills(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)

	def __str__(self):
		return self.name + ' from: ' + self.company


class Location(models.Model):
	street = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100, blank=True)
	country = models.CharField(max_length=150)
	zip = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return self.city + ' : ' + self.street + ' :: ' + self.country


class JobPost(models.Model):
	JOB_TYPE_CHOICES = [
		('Full Time', 'Full Time'),
		('Part Time', 'Part Time'),
	]
	title = models.CharField(max_length=200)
	description = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	expiry = models.DateField(null=True)
	salary = models.IntegerField()
	slug = models.SlugField(null=True, max_length=40, unique=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
	skills = models.ManyToManyField(Skills)
	type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		return super(JobPost, self).save(*args, **kwargs)

	def __str__(self):
		return self.title + ' <' + str(self.salary) + '>'

class Person(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	birthyear = models.IntegerField()
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	slug = models.SlugField(null=True, unique=True, max_length=40)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.firstname + self.lastname + str(self.birthyear))
		return super(Person, self).save(*args, **kwargs)

	def __str__(self):
		return self.firstname + ' ' + self.lastname + ' (from) ' + self.city



#jobpost_9 = author_3.jobpost_set.create(title="Ninth job post", description="Example",
#	salary="9000")
#author_2.jobpost_set.all()
#author_1.jobpost_set.add(job10)
#author_1.jobpost_set.count()
#autor_1.jobpost_set.filter(title__contains="First")
#JobPost.object.filter(author__name__contains="samira")
#JobPost.object.filter(author__name__startswith="samira", author__designation__contains="klba")
#JobPost.objects.filter(author__in=[1,2])