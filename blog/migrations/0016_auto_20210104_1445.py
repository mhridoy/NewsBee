# Generated by Django 3.1.4 on 2021-01-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210104_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]