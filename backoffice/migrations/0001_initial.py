# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Discipline'
        db.create_table(u'backoffice_discipline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('info', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('info_he', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('info_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sidar_id', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'backoffice', ['Discipline'])

        # Adding model 'Designer'
        db.create_table(u'backoffice_designer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('birth_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('death_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('birth_country', self.gf('django_countries.fields.CountryField')(default='IL', max_length=2, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('philosophy', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('philosophy_summary', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('philosophy_summary_he', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('philosophy_summary_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('sidar_id', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('generation_as_choices', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('belongs_to_studio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Designer'], null=True, blank=True)),
        ))
        db.send_create_signal(u'backoffice', ['Designer'])

        # Adding model 'Collector'
        db.create_table(u'backoffice_collector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('birth_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('death_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('birth_country', self.gf('django_countries.fields.CountryField')(default='IL', max_length=2, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('philosophy', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('philosophy_summary', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('philosophy_summary_he', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('philosophy_summary_en', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('sidar_id', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('homepage', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'backoffice', ['Collector'])

        # Adding model 'Work'
        db.create_table(u'backoffice_work', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Designer'], null=True)),
            ('raw_image', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Discipline'], null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Category'], null=True)),
            ('is_self_collected', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('publish_date_as_text', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('publish_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('size_as_text', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('height', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2, blank=True)),
            ('width', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2, blank=True)),
            ('depth', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django_countries.fields.CountryField')(default='IL', max_length=2, null=True, blank=True)),
            ('technique', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description_he', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'backoffice', ['Work'])

        # Adding M2M table for field of_collections on 'Work'
        db.create_table(u'backoffice_work_of_collections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('work', models.ForeignKey(orm[u'backoffice.work'], null=False)),
            ('collector', models.ForeignKey(orm[u'backoffice.collector'], null=False))
        ))
        db.create_unique(u'backoffice_work_of_collections', ['work_id', 'collector_id'])

        # Adding M2M table for field subjects on 'Work'
        db.create_table(u'backoffice_work_subjects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('work', models.ForeignKey(orm[u'backoffice.work'], null=False)),
            ('subject', models.ForeignKey(orm[u'backoffice.subject'], null=False))
        ))
        db.create_unique(u'backoffice_work_subjects', ['work_id', 'subject_id'])

        # Adding model 'Category'
        db.create_table(u'backoffice_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Category'], null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('info_he', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('info_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sidar_id', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'backoffice', ['Category'])

        # Adding model 'Subject'
        db.create_table(u'backoffice_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Subject'], null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'backoffice', ['Subject'])

        # Adding model 'UserProfile'
        db.create_table(u'backoffice_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'backoffice', ['UserProfile'])

        # Adding M2M table for field in_charge_of_designers on 'UserProfile'
        db.create_table(u'backoffice_userprofile_in_charge_of_designers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'backoffice.userprofile'], null=False)),
            ('designer', models.ForeignKey(orm[u'backoffice.designer'], null=False))
        ))
        db.create_unique(u'backoffice_userprofile_in_charge_of_designers', ['userprofile_id', 'designer_id'])


    def backwards(self, orm):
        # Deleting model 'Discipline'
        db.delete_table(u'backoffice_discipline')

        # Deleting model 'Designer'
        db.delete_table(u'backoffice_designer')

        # Deleting model 'Collector'
        db.delete_table(u'backoffice_collector')

        # Deleting model 'Work'
        db.delete_table(u'backoffice_work')

        # Removing M2M table for field of_collections on 'Work'
        db.delete_table('backoffice_work_of_collections')

        # Removing M2M table for field subjects on 'Work'
        db.delete_table('backoffice_work_subjects')

        # Deleting model 'Category'
        db.delete_table(u'backoffice_category')

        # Deleting model 'Subject'
        db.delete_table(u'backoffice_subject')

        # Deleting model 'UserProfile'
        db.delete_table(u'backoffice_userprofile')

        # Removing M2M table for field in_charge_of_designers on 'UserProfile'
        db.delete_table('backoffice_userprofile_in_charge_of_designers')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'backoffice.category': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'info_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backoffice.Category']", 'null': 'True', 'blank': 'True'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'backoffice.collector': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Collector'},
            'birth_country': ('django_countries.fields.CountryField', [], {'default': "'IL'", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'philosophy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'philosophy_summary': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'philosophy_summary_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'philosophy_summary_he': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'backoffice.designer': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Designer'},
            'belongs_to_studio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backoffice.Designer']", 'null': 'True', 'blank': 'True'}),
            'birth_country': ('django_countries.fields.CountryField', [], {'default': "'IL'", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'generation_as_choices': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'philosophy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'philosophy_summary': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'philosophy_summary_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'philosophy_summary_he': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'backoffice.discipline': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Discipline'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'info_en': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'info_he': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'backoffice.subject': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Subject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backoffice.Subject']", 'null': 'True', 'blank': 'True'})
        },
        u'backoffice.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_charge_of_designers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['backoffice.Designer']", 'symmetrical': 'False', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'backoffice.work': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Work'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backoffice.Category']", 'null': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django_countries.fields.CountryField', [], {'default': "'IL'", 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backoffice.Designer']", 'null': 'True'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backoffice.Discipline']", 'null': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_self_collected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'of_collections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['backoffice.Collector']", 'symmetrical': 'False', 'blank': 'True'}),
            'publish_date_as_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'publish_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'raw_image': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100'}),
            'size_as_text': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['backoffice.Subject']", 'symmetrical': 'False', 'blank': 'True'}),
            'technique': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'width': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['backoffice']