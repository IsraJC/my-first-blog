# Generated by Django 2.2.13 on 2020-07-03 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20200703_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='qualification',
            field=models.CharField(blank=True, default=' ', max_length=400),
        ),
    ]
