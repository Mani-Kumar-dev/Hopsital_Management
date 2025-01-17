# Generated by Django 5.0.6 on 2024-06-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('admission_date', models.DateField()),
                ('diagnosis', models.TextField()),
                ('room_number', models.IntegerField()),
                ('discharge_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
