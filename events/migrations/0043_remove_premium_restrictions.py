# Generated by Django 2.0 on 2018-08-25 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0042_allow_team_without_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='is_premium',
        ),
        migrations.RemoveField(
            model_name='team',
            name='premium_by',
        ),
        migrations.RemoveField(
            model_name='team',
            name='premium_expires',
        ),
        migrations.RemoveField(
            model_name='team',
            name='premium_started',
        ),
    ]
