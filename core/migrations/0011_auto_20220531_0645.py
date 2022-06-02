# Generated by Django 3.2.12 on 2022-05-31 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_pin',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
