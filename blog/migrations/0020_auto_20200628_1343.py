# Generated by Django 2.2.13 on 2020-06-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200628_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='number',
            field=models.CharField(blank=True, default='', max_length=11),
        ),
    ]
