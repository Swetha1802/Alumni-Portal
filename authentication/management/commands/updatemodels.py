from django.core.management.base import BaseCommand
import pandas as pd
from authentication.models import User

class Command (BaseCommand):
	help = 'import booms'
	def add_arguments(self, parser):
		pass
	def handle(self, *args, **options):
		df=pd.read_csv('Alumnidetailss.csv')
		for USERNAME, FIRSTNAME, LASTNAME, EMAIL, ROLE, COUNTRY, DEPARTMENT, YEAR, COMPANY, DESIGNATION in zip(df.Username,df.Firstname,df.Lastname, df.Email, df.Role, df.Country, df.Department, df.Year, df.Company, df.Designation):
			models=User(username=USERNAME, first_name=FIRSTNAME, last_name=LASTNAME, email=EMAIL, role=ROLE, country=COUNTRY, department=DEPARTMENT, year=YEAR, company=COMPANY, designation=DESIGNATION )
			models.save()
