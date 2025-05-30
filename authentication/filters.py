import django_filters

from .models import *

class UserFilter(django_filters.FilterSet):
	first_name = django_filters.CharFilter(lookup_expr='icontains',label='First Name')
	last_name = django_filters.CharFilter(lookup_expr='icontains',label='Last Name')
	company = django_filters.CharFilter(lookup_expr='icontains',label='Company')
	designation = django_filters.CharFilter(lookup_expr='icontains',label='Designation')


	class Meta:
		model = User
		fields = ('first_name', 'last_name','country','department','company','year','designation')

class MentorshipFilter(django_filters.FilterSet):
	Project_Title = django_filters.CharFilter(lookup_expr='icontains',label='Project Title')
	Project_Description = django_filters.CharFilter(lookup_expr='icontains',label='Project Description')

	class Meta:
		model = Mentorship
		fields = ('Domain','Project_Description','Project_Title')