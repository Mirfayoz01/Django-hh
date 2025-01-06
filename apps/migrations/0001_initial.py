# Generated by Django 5.1.4 on 2025-01-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('location', models.CharField(max_length=100)),
                ('full_time', models.CharField(max_length=100)),
            ],
        ),
    ]
