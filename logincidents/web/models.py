from django.db import models
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, mail_managers, send_mail, EmailMessage, mail_admins
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings

# Create your models here.


class IncidentDetails(models.Model):
    companyid = models.CharField('Company ID', max_length = 20)
    what_nearly_happened = models.CharField('What nearly happened', max_length = 200)
    why_didnt_really_happen = models.CharField('Why didnt really happen', max_length = 200)
    geo_location = models.FloatField('Geo location', max_length = 50, null = True, blank = True)
    floor_of_building = models.CharField('Floor of Building', max_length = 50)
    building = models.CharField('Building', max_length = 50)
    address = models.TextField('Address', max_length = 200)
    date = models.DateField('Date', max_length = 50)
    time = models.TimeField('Time', max_length = 50)
    description = models.TextField('Description text', max_length = 500)
    phoneid = models.CharField('Phone ID', max_length = 50)
    name = models.CharField('Name', max_length = 50)
    department = models.CharField('Department', max_length = 100)
    worksid = models.CharField('WorksID', max_length = 50)
    photo_media = models.ImageField(upload_to='uploads/images/')
    video_media = models.URLField('Video Media', help_text="Video")

    class Meta:
        verbose_name = 'Incident Details'
        verbose_name_plural = 'Incident Details'    

class MinorIncident(IncidentDetails):

    class Meta:
        verbose_name = 'Minor Incident'
        verbose_name_plural = 'Minor Incidents'

class MajorIncident(IncidentDetails):
    injured_person_name = models.CharField('Injured Person Name', max_length = 50)
    injured_person_role = models.CharField('Injured Person Role', max_length = 50)
    severity = models.CharField('Severity', max_length = 50)
    medical_attention = models.CharField('Medical Attention', max_length = 50)

    class Meta:
        verbose_name = 'Major Incident'
        verbose_name_plural = 'Major Incidents'

class Witness(models.Model):
    majorincident = models.ForeignKey(MajorIncident)
    name = models.CharField('Name', max_length = 50)
    adddress = models.TextField('Address', max_length = 200)
    credentials = models.CharField('Credentials', max_length = 100)
    date_of_birth = models.DateField('Date of Birth', max_length = 50)

    class Meta:
        verbose_name = 'Witness'
        verbose_name_plural = 'Witness'

class InjuryPhotos(models.Model):
    majorincident = models.ForeignKey(MajorIncident)
    name = models.CharField('Name', max_length = 50)
    photo = models.ImageField(upload_to = 'uploads/images/injury/')

    class Meta:
        verbose_name = 'Injury Photos'
        verbose_name_plural = 'Injury Photos'

class Company(models.Model):
    majorincident = models.ForeignKey(MajorIncident, null = True, blank = True)
    minorincident = models.ForeignKey(MinorIncident, null = True, blank = True)
    name = models.CharField('Name', max_length = 50)