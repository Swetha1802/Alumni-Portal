from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponseRedirect
from .models import *
from authentication.models import User
from .forms import JobForm
from .forms import MentorshipForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login



def index(request):
    return render(request,'index.html')

@login_required
def events(request):
    user_list = Event.objects.get_queryset().order_by('title')
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,'events.html',{'users': users})

@login_required
def events_f(request):
    events = Event.objects.all()
    return render(request,'events-f.html',{'events': events})


@login_required
def viewjobs(request):
    jobpostings = JobPostings.objects.all()
    return render(request,'viewjobs.html',{'jobpostings': jobpostings})

@login_required
def viewjobs_f(request):
    jobpostings = JobPostings.objects.all()
    return render(request,'viewjobs-f.html',{'jobpostings': jobpostings})

@login_required
def salumni(request):
    return render(request,'superAlumni.html')

@login_required
def student(request):
    jobpostings = JobPostings.objects.all()
    
    return render(request,'student.html',context)

@login_required
def sstudent(request):
    return render(request,'superStudent.html')

@login_required
def viewmentorship(request):
    mentorship = Mentorship.objects.all()
    return render(request,'viewmentorships.html',{'mentorship': mentorship})

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

@login_required
def addmentorship(request):
    form = MentorshipForm
    submitted = False
    if request.method == "POST":
        form = MentorshipForm (request. POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mentorship?submitted=True')
        else:
            form = MentorshipForm
    if 'submitted' in request.GET:
            submitted = True
    return render(request,'postmentorship.html',{'form': form, 'submitted':submitted })

