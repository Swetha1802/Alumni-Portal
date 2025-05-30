from django.db import models,migrations
from django.contrib.auth.models import User



# Create your models here.
# Create your models here.
class JobPostings (models. Model):
	Job_Title = models. CharField (max_length=200, null=True)
	Company = models. CharField (max_length=200, null=True)
	Job_Description = models. CharField(max_length=1000, null=True)
	Location = models. CharField (max_length=200, null=True)
	Apply_Link = models. CharField(max_length=900, null=True)

	def __str__(self):
		return self.Job_Title

	
class Event (models. Model):
	title = models. CharField (max_length=200, null=True)
	description = models. CharField(max_length=1000, null=True)
	venue = models. CharField (max_length=200, null=True)
	event_date = models.DateField (null=True)
	link = models. CharField(max_length=900, null=True)


	def __str__(self):
	   	return self.title

class Mentorship (models. Model):
	Project_Title = models. CharField (max_length=200, null=True)
	Domain = models. CharField (max_length=200, null=True)
	Project_Description = models. CharField(max_length=1000, null=True)


	def __str__(self):
		return self.Project_Title

