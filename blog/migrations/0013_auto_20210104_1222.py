# Generated by Django 3.1.4 on 2021-01-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210104_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='title',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='url',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
