# Generated by Django 2.2.14 on 2021-10-18 19:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logger', '0019_purge_deleted_instances'),
    ]

    operations = [
        migrations.AddField(
            model_name='xform',
            name='veritree_form_type',
            field=models.CharField(choices=[('socio-economic', 'socio-economic'), ('inventory', 'inventory'), ('none', 'none')], default='none', max_length=25),
        ),
    ]
