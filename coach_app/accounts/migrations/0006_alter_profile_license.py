# Generated by Django 4.2.16 on 2024-11-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='license',
            field=models.CharField(blank=True, choices=[('Uefa PRO', 'Uefa PRO'), ('Uefa A', 'Uefa A'), ('Uefa B', 'Uefa B'), ('Uefa C', 'Uefa C'), ('National C', 'National C'), ('Grassroots D', 'Grassroots D'), ('Без лиценз', 'Без лиценз')], max_length=30, null=True),
        ),
    ]