# Generated by Django 2.1.1 on 2019-01-16 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_auto_20190115_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='middleterm',
            name='is_own_word',
            field=models.BooleanField(default=0),
        ),
    ]
