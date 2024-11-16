# Generated by Django 4.2.16 on 2024-11-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drills', '0002_alter_drill_progression'),
    ]

    operations = [
        migrations.AddField(
            model_name='drill',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='drill',
            name='coaching_points',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='drill',
            name='duration',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='drill',
            name='graphics',
            field=models.ImageField(blank=True, null=True, upload_to='drills/'),
        ),
        migrations.AlterField(
            model_name='drill',
            name='progression',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
