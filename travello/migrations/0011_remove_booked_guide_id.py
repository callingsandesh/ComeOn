# Generated by Django 3.0.1 on 2020-01-09 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0010_booked_guide_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='guide_id',
        ),
    ]
