# Generated by Django 3.1.3 on 2020-11-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Url'),
        ),
    ]
