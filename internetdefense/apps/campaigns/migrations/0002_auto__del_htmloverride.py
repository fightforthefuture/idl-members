# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'HTMLOverride'
        db.delete_table('campaigns_htmloverride')


    def backwards(self, orm):
        # Adding model 'HTMLOverride'
        db.create_table('campaigns_htmloverride', (
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('variant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaigns.Variant'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaigns.Campaign'])),
        ))
        db.send_create_signal('campaigns', ['HTMLOverride'])


    models = {
        'campaigns.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'})
        },
        'campaigns.variant': {
            'Meta': {'object_name': 'Variant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['campaigns']