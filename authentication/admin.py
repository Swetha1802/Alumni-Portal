from django.contrib import admin
from .models import *

# Register your models here.
class FooAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
admin.site.register(User)
admin.site.register(JobPosting,FooAdmin)
admin.site.register(Mentorship)

