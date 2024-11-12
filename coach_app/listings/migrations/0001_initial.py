# Generated by Django 4.2.16 on 2024-11-11 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=50)),
                ('experience_needed', models.PositiveSmallIntegerField()),
                ('licence_required', models.CharField(choices=[('Uefa PRO', 'Uefa PRO'), ('Uefa A', 'Uefa A'), ('Uefa B', 'Uefa B'), ('Uefa C', 'Uefa C'), ('National C', 'National C'), ('Grassroots D', 'Grassroots D'), ('Няма', 'Няма')], max_length=30)),
                ('for_age_group', models.CharField(blank=True, choices=[('U5 - U6', 'U5 - U6'), ('U7 - U8', 'U7 - U8'), ('U9 - U10', 'U9 - U10'), ('U11 - U12', 'U11 - U12'), ('U13 - U14', 'U13 - U14'), ('U15 - U16', 'U15 - U16'), ('U16 - U19', 'U16 - U19'), ('Мъже/Жени', 'Мъже/Жени')], max_length=30, null=True)),
                ('salary', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('contact_person', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=13, validators=[django.core.validators.MinValueValidator(10)])),
            ],
        ),
    ]