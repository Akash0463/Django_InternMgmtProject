# Generated by Django 3.1.5 on 2021-02-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InternMgmtApp', '0002_auto_20210211_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='application_details',
            name='applied_in',
            field=models.CharField(default='', max_length=50),
        ),
    ]