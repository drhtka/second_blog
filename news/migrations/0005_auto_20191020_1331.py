# Generated by Django 2.2.6 on 2019-10-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20191020_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coments',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
    ]