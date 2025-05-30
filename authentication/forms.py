from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django.forms import ModelForm
from .models import JobPosting
from .models import Mentorship



# class UploadProfilePhotoForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('profile_photo', )
#     def __init__(self, *args, **kwargs):
#       super(UploadProfilePhotoForm, self).__init__(*args, **kwargs)

#       self.fields['profile_photo'].widget.attrs['class'] = 'form-control'
        

        

class SignupFormA(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

        fields = ('username', 'email', 'first_name', 'last_name', 'role','country', 'department','year','company','designation')
    def __init__(self, *args, **kwargs):
        super(SignupFormA, self).__init__(*args, **kwargs)

        self.fields['year'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['designation'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class SignupFormS(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'role','last_name')
    def __init__(self, *args, **kwargs):
        super(SignupFormS, self).__init__(*args, **kwargs)
 
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class JobForm (ModelForm):
    class Meta:
        model = JobPosting
        fields = ["Job_Title", "Company", "Job_Description", "Location","Apply_Link"]
        # labels={
        # 'job_title'= ' '
        # 'company'=' '
        # 'job_description'=' '
        # 'location'=' '
        # 'apply_link'=' '
        # }


        widgets={
        'Job_Title': forms.TextInput(attrs={'class':'form-control'}),
        'Company': forms.TextInput(attrs={'class':'form-control'}),
        'Job_Description': forms.TextInput(attrs={'class':'form-control'}),
        'Location': forms.TextInput(attrs={'class':'form-control'}),
        'Apply_Link': forms.TextInput(attrs={'class':'form-control'}),


        }

class MentorshipForm (ModelForm):
    class Meta:
        model = Mentorship
        fields = ["Project_Title", "Project_Description", "Domain"]
        def __init__(self, *args, **kwargs):
            super(MentorshipForm, self).__init__(*args, **kwargs)

            self.fields['Project_Title'].widget.attrs['class'] = 'form-control'
            self.fields['Project_Description'].widget.attrs['class'] = 'form-control'
            self.fields['Domain'].widget.attrs['class'] = 'form-control'
        
    


