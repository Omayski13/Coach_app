# Generated by Django 4.2.16 on 2024-11-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='license',
            field=models.CharField(blank=True, choices=[('Uefa PRO', 'Uefa PRO'), ('Uefa A', 'Uefa A'), ('Uefa B', 'Uefa B'), ('Uefa C', 'Uefa C'), ('National C', 'National C'), ('Grassroots D', 'Grassroots D'), ('Няма', 'Няма')], max_length=30, null=True),
        ),
    ]