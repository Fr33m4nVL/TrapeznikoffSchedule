# Generated by Django 3.1.2 on 2020-12-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20200921_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='hand_over_date',
            new_name='deadline',
        ),
    ]
