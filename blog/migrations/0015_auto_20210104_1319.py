# Generated by Django 3.1.4 on 2021-01-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210104_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='url',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='savecountry',
            name='s_count',
            field=models.TextField(max_length=2, unique=True),
        ),
    ]
