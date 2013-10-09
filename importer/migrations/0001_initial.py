# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'importer_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_path', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'importer', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'importer_item')


    models = {
        u'importer.item': {
            'Meta': {'object_name': 'Item'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'full_path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['importer']