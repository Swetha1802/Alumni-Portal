from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Event)
admin.site.register(JobPostings)
admin.site.register(Mentorship)