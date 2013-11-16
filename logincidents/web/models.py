from django.db import models
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, mail_managers, send_mail, EmailMessage, mail_admins
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings

# Create your models here.


class Minorincident(models.Model):
	# companyid = 
	what_nearly_happened = models.CharField('What nearly happened', max_length = 200, null = True, blank = True)
	why_didnt_really_happen = models.CharField('Why didnt really happen', max_length = 200, null = True, blank = True )
	geo_location = models.FloatField('Geo location', max_length = 50, null = True, blank = True)
	floor_of_building = models.CharField('Floor of Building', max_length = 50, null = True, blank = True )
	building = models.CharField('Building', max_length = 50, null = True, blank = True)
	address = models.TextField('Address', max_length = 200, null = True, blank = True)
	date = models.DateField('Date', max_length = 50, null = True, blank = True)
	time = models.TimeField('Time', max_length = 50, null = True, blank = True)
	description = models.TextField('Description text', max_length = 500)
	phoneid = models.CharField('Phone ID', max_length = 50)
	name = models.CharField('Name', max_length = 50)
	department = models.CharField('Department', max_length = 100)
	worksid = models.CharField('WorksID', max_length = 50)
	photo_media = models.ImageField(upload_to='uploads/images/')
	# Video Media - numerous
