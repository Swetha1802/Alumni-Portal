from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image
from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL
class User(AbstractUser):
    ALUMNI = 'ALUMNI'
    STUDENT = 'STUDENT'
  
    ROLE_CHOICES = (
        (ALUMNI, 'Alumni'),
        (STUDENT, 'Student'),
    )



    CSE = 'Computer Science and Engineering'
    IT = 'Information Technology'
    ECE = 'Electronics and Communications Engineering'
    EEE = 'Electricals and Electronics Engineering'

    DEPARTMENT_CHOICES = (
        (CSE, 'Computer Science and Engineering'),
        (IT, 'Information Technology'),
        (ECE, 'Electronics and Communications Engineering'),
        (EEE, 'Electricals and Electronics Engineering'),

    )

    # profile_photo = models.ImageField(blank=True, null=True, default='default-avatar.png')

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    country = CountryField(blank=True, null=True)
    department = models.CharField(blank=True, max_length=100, choices=DEPARTMENT_CHOICES)
    year = models.IntegerField(max_length=4,blank=True, null=True )
    company = models.CharField(max_length=100,blank=True, null=True )
    designation = models.CharField(max_length=100,blank=True, null=True )



    # IMAGE_MAX_SIZE = (150, 150)




    # def resize_image(self):
    #     profile_photo = Image.open(self.profile_photo)
    #     profile_photo.thumbnail(self.IMAGE_MAX_SIZE)
    #     # save the resized image to the file system
    #     # this is not the model save method!
    #     profile_photo.save(self.profile_photo.path)

    # def save(self, *args, **kwargs):
    # 	super().save(*args, **kwargs)
    # 	self.resize_image()


class JobPosting (models. Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Job_Title = models. CharField (max_length=200, null=True)
    Company = models. CharField (max_length=200, null=True)
    Job_Description = models. CharField(max_length=1000, null=True)
    Location = models. CharField (max_length=200, null=True)
    Apply_Link = models. CharField(max_length=900, null=True)

    def __str__(self):
        return self.Job_Title

class Mentorship (models. Model):
    AI = 'Artificial Intelligence'
    ML = 'Machine Learing'
    DS = 'Data Science'
    WEBDEV  = 'Web Development'
    ROBAUT = 'Robotics and Automation'
    RPA = 'Robotics Process and Automation'
    Electricals = 'Electricals'
    Electronics = 'Electronics'
    Civil = 'Civil'
    Mechanical = 'Mechanical'
    Others = 'Others'

    DOMAIN_CHOICES = (
        (AI, 'Artificial Intelligence'),
        (ML, 'Machine Learing'),
        (DS, 'Data Science'),
        (WEBDEV, 'Web Development'),
        (ROBAUT, 'Robotics and Automation'),
        (RPA, 'Robotics Process and Automation'),
        (Electricals, 'Electricals'),
        (Electronics, 'Electronics'),
        (Civil, 'Civil'),
        (Mechanical, 'Mechanical'),
        (Others, 'Others'),


    )
    user = models.ForeignKey('User',on_delete=models.CASCADE,null=True)
    Project_Title = models. CharField (max_length=200, null=True)
    Domain = models.CharField(max_length=100, choices=DOMAIN_CHOICES)
    Project_Description = models. TextField(max_length=1000, null=True)


    def __str__(self):
        return self.Project_Title
