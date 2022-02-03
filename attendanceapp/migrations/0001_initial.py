# Generated by Django 3.2.9 on 2022-02-03 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('join_date', models.DateTimeField(verbose_name='date joined')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateTimeField(verbose_name='date logged')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendanceapp.person')),
            ],
        ),
    ]
