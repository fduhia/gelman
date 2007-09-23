from django.db import models
from tagging.models import Tag

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
	isbn = models.CharField(maxlength=10, primary_key=True)
	title = models.CharField(maxlength=255)
	authors = models.ManyToManyField(Author)
	pages = models.IntegerField()
	publisher = models.ForeignKey(Publisher)
	pub_date = models.DateField()
	timestamp = models.DateTimeField()
	thumb = models.ImageField(upload_to="images")
	cover = models.ImageField(upload_to="images")
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

	class Admin:
		pass


class FileType(models.Model):
	type = models.CharField(maxlength=10)

	def __str__(self):
		return self.type

	class Admin:
		pass


class File(models.Model):
	type = models.ForeignKey(FileType)
	handle = models.FileField(upload_to="files")
	meta = models.ForeignKey(Book)
	
	def __str__(self):
		return self.get_handle_url()

	class Admin:
		pass
