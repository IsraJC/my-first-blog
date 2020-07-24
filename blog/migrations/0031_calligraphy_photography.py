# Generated by Django 2.2.13 on 2020-07-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20200708_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='calligraphy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/calligraphy/')),
            ],
        ),
        migrations.CreateModel(
            name='photography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/photography/')),
            ],
        ),
    ]
