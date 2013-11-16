# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Minorincident'
        db.create_table(u'web_minorincident', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('what_nearly_happened', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('why_didnt_really_happen', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('geo_location', self.gf('django.db.models.fields.FloatField')(max_length=50, null=True, blank=True)),
            ('floor_of_building', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(max_length=50, null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.TimeField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('phoneid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('worksid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo_media', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'web', ['Minorincident'])

    def backwards(self, orm):
        # Deleting model 'Minorincident'
        db.delete_table(u'web_minorincident')

    models = {
        u'web.minorincident': {
            'Meta': {'object_name': 'Minorincident'},
            'address': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'floor_of_building': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'geo_location': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phoneid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo_media': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.TimeField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'what_nearly_happened': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'why_didnt_really_happen': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'worksid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['web']