# Generated by Django 3.2.7 on 2021-09-19 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_auto_20210919_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='compensation',
            new_name='compensation_Details',
        ),
    ]
