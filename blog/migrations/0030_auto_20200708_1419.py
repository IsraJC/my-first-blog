# Generated by Django 2.2.13 on 2020-07-08 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_activities'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activities',
            new_name='Activity',
        ),
    ]