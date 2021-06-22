from django.db import models

# Create your models here.


class Halls(models.Model):
	Name = models.CharField(max_length=50)
	Location = models.CharField(max_length=100)
	rating = models.FloatField(default = 0.0)
	votes = models.IntegerField(default = 0)
	contact = models.CharField(max_length=12, default='No contact available')
	url = models.URLField(max_length=500, default="No location available")
	photo = models.ImageField(upload_to='ticketapp/images', default="No image available")

	def __str__(self):
		return self.Name


class Movie(models.Model):
	Name = models.CharField(max_length=50)
	Category = models.CharField(max_length=50, default='Thriller')
	Directed_by = models.CharField(max_length=20)
	Produced_by = models.CharField(max_length=20)
	Written_by = models.CharField(max_length=20)
	Thumbnail = models.ImageField(upload_to='ticketapp/images', )
	Price = models.FloatField(null=False)
	promo = models.URLField(max_length=200)
	loc = models.ManyToManyField(Halls)

	def __str__(self):
		return self.Name


class Userdata(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	choice = models.ManyToManyField(Movie)
	transaction = models.IntegerField(default=0)

	def __str__(self):
		return self.username
