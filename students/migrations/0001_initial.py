# Generated by Django 5.0.6 on 2024-07-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_number', models.PositiveBigIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('fields_of_study', models.CharField(max_length=50)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
