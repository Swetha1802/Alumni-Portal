from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name="index"),
     path('events/',views.events, name="events"),
     path('alumni/',views.addjob, name="alumni"),
     path('mentorship/',views.addmentorship, name="mentorship"),
     path('salumni/',views.salumni,name="salumni"),
     path('student/',views.student, name="student"),
     path('sstudent/',views.sstudent,name="sstudent"),


    #  path('login/',views.login_view, name='login_view'),
    # path('register/',views.register, name='register'),
    

]