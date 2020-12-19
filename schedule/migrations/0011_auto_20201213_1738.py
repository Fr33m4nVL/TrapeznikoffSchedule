# Generated by Django 3.1.4 on 2020-12-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_subject_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='colors',
            field=models.IntegerField(blank=True, choices=[(1, 'Gray'), (2, 'Red'), (3, 'Yellow'), (4, 'Green'), (5, 'Blue'), (6, 'Indigo'), (7, 'Purple'), (8, 'Pink')], null=True),
        ),
    ]