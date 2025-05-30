from django import forms
from django.forms import ModelForm
from .models import JobPostings
from .models import Mentorship

class JobForm (ModelForm):
    class Meta:
        model = JobPostings
        fields = ["Job_Title", "Company", "Job_Description", "Location","Apply_Link"]
        # labels={
        # 'job_title'= ' '
        # 'company'=' '
        # 'job_description'=' '
        # 'location'=' '
        # 'apply_link'=' '
        # }


        widgets={
        'Job title': forms.TextInput(attrs={'class':'form-control'}),
        'Company': forms.TextInput(attrs={'class':'form-control'}),
        'Job Description': forms.TextInput(attrs={'class':'form-control'}),
        'Location': forms.TextInput(attrs={'class':'form-control'}),
        'Apply Link': forms.TextInput(attrs={'class':'form-control'}),


        }

class MentorshipForm (ModelForm):
    class Meta:
        model = Mentorship
        fields = "__all__"
    


        widgets={
        'Project Title': forms.TextInput(attrs={'class':'form-control'}),
        'Project Description': forms.TextInput(attrs={'class':'form-control'}),
        'Domain': forms.TextInput(attrs={'class':'form-control'}),

        }
