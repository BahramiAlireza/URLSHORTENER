# Generated by Django 3.1.3 on 2021-09-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlobject',
            name='user',
        ),
        migrations.AlterField(
            model_name='urlobject',
            name='shorten_url',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
