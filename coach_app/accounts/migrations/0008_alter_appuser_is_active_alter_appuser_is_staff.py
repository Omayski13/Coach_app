# Generated by Django 4.2.16 on 2024-11-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_appuser_is_active_appuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
