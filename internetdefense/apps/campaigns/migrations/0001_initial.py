# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Variant'
        db.create_table('campaigns_variant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=16)),
        ))
        db.send_create_signal('campaigns', ['Variant'])

        # Adding model 'Campaign'
        db.create_table('campaigns_campaign', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=32)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('campaigns', ['Campaign'])

        # Adding model 'HTMLOverride'
        db.create_table('campaigns_htmloverride', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaigns.Variant'])),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['campaigns.Campaign'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('campaigns', ['HTMLOverride'])


    def backwards(self, orm):
        # Deleting model 'Variant'
        db.delete_table('campaigns_variant')

        # Deleting model 'Campaign'
        db.delete_table('campaigns_campaign')

        # Deleting model 'HTMLOverride'
        db.delete_table('campaigns_htmloverride')


    models = {
        'campaigns.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'})
        },
        'campaigns.htmloverride': {
            'Meta': {'object_name': 'HTMLOverride'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaigns.Campaign']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaigns.Variant']"})
        },
        'campaigns.variant': {
            'Meta': {'object_name': 'Variant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['campaigns']