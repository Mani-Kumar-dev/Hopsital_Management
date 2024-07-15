# Generated by Django 5.0.6 on 2024-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperationTheatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_ID', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Disease', models.CharField(max_length=100)),
                ('Type_of_Surgery', models.CharField(max_length=100)),
                ('Surgery_Doctors', models.CharField(max_length=255)),
                ('Surgery_Nurses', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]