# coding: utf-8
from __future__ import unicode_literals, print_function, division, absolute_import
# coding: utf-8
from __future__ import unicode_literals, print_function, division, absolute_import
from south.db import db
from south.v2 import SchemaMigration

from onadata.libs.data.db import rename_table_pending_creates


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('odk_viewer_columnrename', 'viewer_columnrename')
        db.rename_table('odk_viewer_export', 'viewer_export')
        db.rename_table('odk_viewer_instancemodification',
                       'viewer_instancemodification')
        db.rename_table('odk_viewer_parsedinstance', 'viewer_parsedinstance')

        rename_table_pending_creates('odk_viewer', 'viewer')

    def backwards(self, orm):
        db.rename_table('viewer_columnrename', 'odk_viewer_columnrename')
        db.rename_table('viewer_export', 'odk_viewer_export')
        db.rename_table('viewer_instancemodification',
                       'viewer_instancemodification')
        db.rename_table('viewer_parsedinstance', 'odk_viewer_parsedinstance')

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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'logger.instance': {
            'Meta': {'object_name': 'Instance'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryCollectionField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "u'submitted_via_web'", 'max_length': '20'}),
            'survey_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['logger.SurveyType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '249'}),
            'xform': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'null': 'True', 'to': "orm['logger.XForm']"}),
            'xml': ('django.db.models.fields.TextField', [], {})
        },
        'logger.surveytype': {
            'Meta': {'object_name': 'SurveyType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'logger.xform': {
            'Meta': {'ordering': "('id_string',)", 'unique_together': "(('user', 'id_string'), ('user', 'sms_id_string'))", 'object_name': 'XForm'},
            'allows_sms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bamboo_dataset': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '60'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "u''", 'null': 'True'}),
            'downloadable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'encrypted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_start_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_string': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'instances_with_geopoints': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_crowd_form': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'json': ('django.db.models.fields.TextField', [], {'default': "u''"}),
            'last_submission_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'num_of_submissions': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'shared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shared_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sms_id_string': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'xforms'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32'}),
            'xls': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'xml': ('django.db.models.fields.TextField', [], {})
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
        },
        'viewer.columnrename': {
            'Meta': {'object_name': 'ColumnRename'},
            'column_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'xpath': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'viewer.export': {
            'Meta': {'unique_together': "(('xform', 'filename'),)", 'object_name': 'Export'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'export_type': ('django.db.models.fields.CharField', [], {'default': "'xls'", 'max_length': '10'}),
            'export_url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'filedir': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '1'}),
            'task_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_of_last_submission': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'xform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['logger.XForm']"})
        },
        'viewer.instancemodification': {
            'Meta': {'object_name': 'InstanceModification'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'modifications'", 'to': "orm['logger.Instance']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'xpath': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'viewer.parsedinstance': {
            'Meta': {'object_name': 'ParsedInstance'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'parsed_instance'", 'unique': 'True', 'to': "orm['logger.Instance']"}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lng': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        }
    }

    complete_apps = ['viewer']
