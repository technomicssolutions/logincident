# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IncidentDetails'
        db.create_table(u'web_incidentdetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('companyid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('what_nearly_happened', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('why_didnt_really_happen', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('geo_location', self.gf('django.db.models.fields.FloatField')(max_length=50, null=True, blank=True)),
            ('floor_of_building', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')(max_length=50)),
            ('time', self.gf('django.db.models.fields.TimeField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('phoneid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('worksid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo_media', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('video_media', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'web', ['IncidentDetails'])

        # Adding model 'MinorIncident'
        db.create_table(u'web_minorincident', (
            (u'incidentdetails_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.IncidentDetails'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'web', ['MinorIncident'])

        # Adding model 'MajorIncident'
        db.create_table(u'web_majorincident', (
            (u'incidentdetails_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web.IncidentDetails'], unique=True, primary_key=True)),
            ('injured_person_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('injured_person_role', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('medical_attention', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'web', ['MajorIncident'])

        # Adding model 'Witness'
        db.create_table(u'web_witness', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('majorincident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.MajorIncident'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('adddress', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('credentials', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(max_length=50)),
        ))
        db.send_create_signal(u'web', ['Witness'])

        # Adding model 'InjuryPhotos'
        db.create_table(u'web_injuryphotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('majorincident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.MajorIncident'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'web', ['InjuryPhotos'])

        # Adding model 'Company'
        db.create_table(u'web_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('majorincident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.MajorIncident'], null=True, blank=True)),
            ('minorincident', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.MinorIncident'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'web', ['Company'])

    def backwards(self, orm):
        # Deleting model 'IncidentDetails'
        db.delete_table(u'web_incidentdetails')

        # Deleting model 'MinorIncident'
        db.delete_table(u'web_minorincident')

        # Deleting model 'MajorIncident'
        db.delete_table(u'web_majorincident')

        # Deleting model 'Witness'
        db.delete_table(u'web_witness')

        # Deleting model 'InjuryPhotos'
        db.delete_table(u'web_injuryphotos')

        # Deleting model 'Company'
        db.delete_table(u'web_company')

    models = {
        u'web.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'majorincident': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.MajorIncident']", 'null': 'True', 'blank': 'True'}),
            'minorincident': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.MinorIncident']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.incidentdetails': {
            'Meta': {'object_name': 'IncidentDetails'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'companyid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'date': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'floor_of_building': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'geo_location': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phoneid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo_media': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.TimeField', [], {'max_length': '50'}),
            'video_media': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'what_nearly_happened': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'why_didnt_really_happen': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'worksid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.injuryphotos': {
            'Meta': {'object_name': 'InjuryPhotos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'majorincident': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.MajorIncident']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'web.majorincident': {
            'Meta': {'object_name': 'MajorIncident', '_ormbases': [u'web.IncidentDetails']},
            u'incidentdetails_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.IncidentDetails']", 'unique': 'True', 'primary_key': 'True'}),
            'injured_person_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'injured_person_role': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'medical_attention': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'web.minorincident': {
            'Meta': {'object_name': 'MinorIncident', '_ormbases': [u'web.IncidentDetails']},
            u'incidentdetails_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web.IncidentDetails']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'web.witness': {
            'Meta': {'object_name': 'Witness'},
            'adddress': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'credentials': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'majorincident': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.MajorIncident']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']