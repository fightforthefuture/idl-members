# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Impression.is_autobroadcast'
        db.add_column('analytics_impression', 'is_autobroadcast',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Impression.is_autobroadcast'
        db.delete_column('analytics_impression', 'is_autobroadcast')


    models = {
        'analytics.impression': {
            'Meta': {'object_name': 'Impression'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaigns.Campaign']", 'null': 'True', 'blank': 'True'}),
            'custom_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'embedding_host': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'embedding_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'is_autobroadcast': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaigns.Variant']", 'null': 'True', 'blank': 'True'})
        },
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

    complete_apps = ['analytics']