# Generated by Django 2.0.2 on 2018-02-09 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_logger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dbloggermodel',
            old_name='bio',
            new_name='method',
        ),
    ]
