# Generated by Django 3.1.4 on 2020-12-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20201206_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]