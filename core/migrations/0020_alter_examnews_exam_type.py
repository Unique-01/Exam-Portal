# Generated by Django 3.2.12 on 2022-08-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20220812_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examnews',
            name='exam_type',
            field=models.CharField(choices=[('neco', 'neco'), ('waec', 'waec'), ('jupeb', 'jupeb'), ('nabteb', 'nabteb'), ('frontpage', 'frontpage')], default='', max_length=10),
        ),
    ]