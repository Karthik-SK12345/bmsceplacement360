# Generated by Django 3.2.7 on 2021-09-19 11:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0023_alter_post_additional_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Additional_Topics',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]