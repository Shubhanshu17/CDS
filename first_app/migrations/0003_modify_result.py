# Generated by Django 2.0 on 2018-09-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_remove_result_chin_ups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modify_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Person_Name', models.CharField(max_length=15)),
                ('Pull_Ups', models.IntegerField()),
                ('Push_Ups', models.IntegerField()),
                ('Chin_Ups', models.IntegerField()),
            ],
        ),
    ]
