# Generated by Django 3.2.5 on 2021-07-30 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20210730_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Url'),
        ),
    ]