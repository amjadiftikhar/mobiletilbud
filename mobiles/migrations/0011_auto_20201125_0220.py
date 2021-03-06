# Generated by Django 3.1.3 on 2020-11-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0010_auto_20201125_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilecameraspecification',
            name='back_cam_aperture',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Rear Camera Aperture'),
        ),
        migrations.AlterField(
            model_name='mobilecameraspecification',
            name='front_cam_aperture',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='front_camera_aperture'),
        ),
        migrations.AlterField(
            model_name='mobilecameraspecification',
            name='front_cam_megapixel',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='front_camera_megapixel'),
        ),
        migrations.AlterField(
            model_name='mobilecameraspecification',
            name='front_cam_video_resolution',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='front_camera_video_resolution'),
        ),
        migrations.AlterField(
            model_name='mobilecameraspecification',
            name='rear_cam_megapixel',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='rear_camera_megapixel'),
        ),
        migrations.AlterField(
            model_name='mobilecameraspecification',
            name='rear_cam_video_resolution',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='rear_camera_video_resolution'),
        ),
    ]
