"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import authentication.views
import alumni.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumni.urls'), name="home"),
    path('index/', alumni.views.index, name='index'),    
    
    path('signup-alumni/', authentication.views.signup_page_a, name='signup'),
    path('signup-student/', authentication.views.signup_page_s, name='signup-f'),

    path('profile-photo/upload', authentication.views.upload_profile_photo,name='upload_profile_photo'),
    path('profile-photo-f/upload', authentication.views.upload_profile_photo_f,name='upload_profile_photo-f'),
    path('login/', authentication.views.login_page, name='login'),
    path('events/', alumni.views.events, name='events'),
    path('events-f/', alumni.views.events_f, name='events-f'),
    path('view-ment/', authentication.views.t_filter, name='ment'),
    path('post-jobs/',authentication.views.addjob,name="postjobs"),
    path('view-jobs/',authentication.views.viewjobs,name="viewjobs"),
    path('view-jobs-f/',authentication.views.viewjobs_f,name="viewjobs-f"),
    path('post-mentorship/',authentication.views.addmentorship,name="post-mentorship"),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('salumni/', alumni.views.salumni, name='salumni'),
    path('sstudent/', alumni.views.sstudent, name='sstudent'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('change-password-f/', PasswordChangeView.as_view(
        template_name='authentication/password_change_f.html'),
         name='password_change-f'
         ),
    path('change-password-d/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_d.html'),
         name='password_change-d'
         ),
    path('members/', authentication.views.members, name='members'),
    path('members/details/<str:username>', authentication.views.details, name='details'),
    path('filter/', authentication.views.to_filter, name='filter'),
    


]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


