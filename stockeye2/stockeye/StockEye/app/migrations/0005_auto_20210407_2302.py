# Generated by Django 3.1.7 on 2021-04-08 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210407_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocklist',
            old_name='postiveSentimentCount',
            new_name='positiveSentimentCount',
        ),
    ]
