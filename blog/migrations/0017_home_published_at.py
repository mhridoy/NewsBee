# Generated by Django 3.1.4 on 2021-01-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20210104_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='published_at',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
