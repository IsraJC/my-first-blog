# Generated by Django 2.2.13 on 2020-06-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
