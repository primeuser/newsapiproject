# Generated by Django 2.1.7 on 2019-03-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_auto_20190319_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
