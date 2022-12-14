# Generated by Django 3.1.4 on 2021-05-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='PoshanVatikaPics/')),
                ('name', models.CharField(default='', max_length=100)),
                ('nutri_nm', models.CharField(default='', max_length=100)),
                ('area', models.IntegerField()),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=8, null=True)),
                ('lat', models.CharField(max_length=15)),
                ('lng', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UploadWellPictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='WellPics/')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('well_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('radius', models.IntegerField(blank=True, null=True)),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=8, null=True)),
                ('lat', models.CharField(max_length=15)),
                ('lng', models.CharField(max_length=15)),
            ],
        ),
    ]
