from django.db import models

# Create your models here.

class Article(models.Model):
	headline = models.CharField(max_length=255)
	slug = models.SlugField(max_length=30)
	organization = models.CharField(max_length=50)
	byline = models.CharField(max_length=50)
	date = models.DateTimeField(blank=True, null=True)
	hyperlink = models.CharField(max_length=255)
	#If there's really a ulr longer than 255 we'll shorten that shit
	impact = models.ManyToManyField('Impact')
	training = models.ManyToManyField('Training', blank=True, null=True, related_name="events+")
	description = models.TextField()

	def __unicode__(self):
		return '%s | %s' %(self.headline, self.organization)

	def get_absolute_url(self):
		return "/articles/%i/" % self.slug

class Impact(models.Model):
	name = models.CharField(max_length=20)
	slug = models.SlugField(max_length=20)

	def __unicode__(self):
		return '%s' %(self.name)

class Training(models.Model):
	slug = models.SlugField(max_length=30)
	type = models.ForeignKey('TrainingType')
	date = models.DateTimeField(blank=True, null=True)
	city = models.CharField(max_length=50)
	lat = models.CharField(max_length=10, blank=True)
	lng = models.CharField(max_length=10, blank=True)
	host = models.CharField(max_length=255, blank=True)
	attendance = models.IntegerField(blank=True, null=True)
	#trainers = models.CharField(max_length=2255, blank=True)
	#description = models.TextField()
	article = models.ManyToManyField('Article', blank=True, null=True, related_name="stories+")
	
	def __unicode__(self):
		return '%s %s | %s/%s/%s' %(self.city, self.type, self.date.day, self.date.month, self.date.year,)

class TrainingType(models.Model):
	name = models.CharField(max_length=20)
	slug = models.SlugField(max_length=20)
	
	def __unicode__(self):
		return '%s' %(self.name)

		