# Generated by Django 2.2.6 on 2019-10-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.Tag', verbose_name='Теги'),
        ),
    ]
