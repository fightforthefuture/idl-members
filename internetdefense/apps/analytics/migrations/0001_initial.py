# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Impression'
        db.create_table('analytics_impression', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaigns.Campaign'], null=True, blank=True)),
            ('embedding_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('embedding_host', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('custom_url', self.gf('django.db.models.fields.URLField')(max_length=1024, null=True, blank=True)),
            ('variant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaigns.Variant'], null=True, blank=True)),
        ))
        db.send_create_signal('analytics', ['Impression'])


    def backwards(self, orm):
        # Deleting model 'Impression'
        db.delete_table('analytics_impression')


    models = {
        'analytics.impression': {
            'Meta': {'object_name': 'Impression'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaigns.Campaign']", 'null': 'True', 'blank': 'True'}),
            'custom_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'embedding_host': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'embedding_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
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