# Generated by Django 3.1.1 on 2020-09-21 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20200921_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='homework',
        ),
        migrations.AddField(
            model_name='homework',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='schedule.subject'),
        ),
    ]
