# Generated by Django 2.1.4 on 2018-12-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='age',
            field=models.IntegerField(default=1),
        ),
    ]
