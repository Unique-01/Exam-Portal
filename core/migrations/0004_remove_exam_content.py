# Generated by Django 3.2.12 on 2022-05-28 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_body_exam_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='content',
        ),
    ]