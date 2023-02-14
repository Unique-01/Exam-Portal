# Generated by Django 3.2.12 on 2022-08-12 01:40

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_exam_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('exam_type', models.CharField(choices=[('LOADING...', 'loading'), ('UPDATED', 'updated')], default='', max_length=10)),
            ],
        ),
    ]