# Generated by Django 2.1.1 on 2019-01-15 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suffix',
            old_name='gender',
            new_name='needs_s',
        ),
    ]
