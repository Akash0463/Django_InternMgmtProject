# Generated by Django 3.1.5 on 2021-02-15 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InternMgmtApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='applied_in',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='resume',
        ),
    ]