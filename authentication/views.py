from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .filters import UserFilter
from .filters import MentorshipFilter
from django.http import HttpResponseRedirect
from .forms import MentorshipForm
from django.http import HttpResponse
from django.template import loader


from .models import*
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import JobForm


def signup_page_a(request):
    form = forms.SignupFormA()
    if request.method == 'POST':
        form = forms.SignupFormA(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if user is not None and user.role=="ALUMNI":
                login(request, user)
                return redirect('salumni')
            elif user is not None and user.role=="STUDENT":
            	login(request, user)
            	return redirect('sstudent')
            else:
                message = 'Login failed!'
    return render(request, 'authentication/signup-alumni.html', context={'form': form})

def signup_page_s(request):
    form = forms.SignupFormS()
    if request.method == 'POST':
        form = forms.SignupFormS(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            if user is not None and user.role=="ALUMNI":
                login(request, user)
                return redirect('salumni')
            elif user is not None and user.role=="STUDENT":
                login(request, user)
                return redirect('sstudent')
            else:
                message = 'Login failed!'
    return render(request, 'authentication/signup-student.html', context={'form': form})

def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # return redirect('home')
            
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})


def to_filter(request):

    users = User.objects.filter(role="ALUMNI")
    myFilter = UserFilter(request.GET, queryset=users)
    users = myFilter.qs


    context = {'myFilter': myFilter}
    return render(request, 'all_members.html', context)

def members(request):
  mymembers = User.objects.filter(role="ALUMNI")
  
  users = User.objects.filter(role="ALUMNI")
  myFilter = UserFilter(request.GET, queryset=users)
  users = myFilter.qs
  qd = request.GET.copy()
  qd.pop('page', None)
  querystring = qd.urlencode()
  paginator = Paginator(users, 12)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
    'myFilter': myFilter,
    'users': users,
    'page_obj' : page_obj,
    'querystring': querystring,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, username):
  try:
    mymember = User.objects.filter(role="ALUMNI").get(username=username)
  except User.DoesNotExist:
    mymember = None
  template = loader.get_template('member.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

@login_required
def viewjobs(request):
    jobposting = JobPosting.objects.all()
    return render(request,'viewjobs.html',{'jobposting': jobposting})

@login_required
def viewjobs_f(request):
    jobposting = JobPosting.objects.all()
    return render(request,'viewjobs-f.html',{'jobposting': jobposting})

@login_required
def viewmentorship(request):
    mentorship = Mentorship.objects.all()
    return render(request,'viewmentorships.html',{'mentorship': mentorship})

def t_filter(request):

    ments = Mentorship.objects.all()
    mFilter = MentorshipFilter(request.GET, queryset=ments)
    ments = mFilter.qs


    context = {'mFilter': mFilter}
    return render(request, 'viewmentorships.html', context)

@login_required
def addjob(request):
    form = JobForm
    submitted = False
    if request.method == "POST":
        form = JobForm (request. POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/alumni?submitted=True')
        else:
            form = JobForm
    if 'submitted' in request.GET:
            submitted = True
    return render(request,'postjobs.html',{'form': form, 'submitted':submitted })

def upload_profile_photo_f(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # return redirect('home')
            
    return render(request, 'authentication/upload_profile_photo-f.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')



def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None and user.role=="ALUMNI":
                login(request, user)
                return redirect('salumni')
            elif user is not None and user.role=="STUDENT":
            	login(request, user)
            	return redirect('sstudent')
            else:
                message = 'Login failed! Credentials are invalid'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})

@login_required
def addmentorship(request):
    form = MentorshipForm
    submitted = False
    if request.method == "POST":
        form = MentorshipForm (request. POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/mentorship?submitted=True')
        else:
            form = MentorshipForm
    if 'submitted' in request.GET:
            submitted = True
    return render(request,'postmentorship.html',{'form': form, 'submitted':submitted })
