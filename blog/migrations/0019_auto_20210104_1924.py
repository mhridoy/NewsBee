# Generated by Django 3.1.4 on 2021-01-04 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_share'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
