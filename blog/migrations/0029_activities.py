# Generated by Django 2.2.13 on 2020-07-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20200706_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
