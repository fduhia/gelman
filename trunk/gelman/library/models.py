from django.db import models

# NOTE: maxlength is obsolete in >0.96, replaced by max_length

class Author(models.Model):
	# Refactor me as first, last
	name = models.CharField(maxlength=64)
	
	def __str__(self):
		return self.name

	class Admin:
		pass


class Publisher(models.Model):
	name = models.CharField(maxlength=64)

	def __str__(self):
		return self.name

	class Admin:
		pass


class Book(models.Model):
	isbn13 = models.CharField(maxlength=13, primary_key=True)
	name = models.CharField(maxlength=255)
	authors = models.ManyToManyField(Author)
	pages = models.IntegerField()
	publisher = models.ForeignKey(Publisher)
	pub_date = models.DateTimeField('data published')

	def __str__(self):
		return self.name

	class Admin:
		pass

# Create your models here.
