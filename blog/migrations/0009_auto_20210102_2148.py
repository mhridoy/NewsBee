# Generated by Django 3.1.4 on 2021-01-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210102_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='slug',
        ),
        migrations.AddField(
            model_name='home',
            name='url',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
