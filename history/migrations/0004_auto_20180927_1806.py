# Generated by Django 2.1.1 on 2018-09-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_auto_20180927_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chathistory',
            name='date',
            field=models.DateTimeField(default='2018-09-27 18:06'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='date',
            field=models.DateTimeField(default='2018-09-27 18:06'),
        ),
        migrations.AlterField(
            model_name='personalmessage',
            name='date',
            field=models.DateTimeField(default='2018-09-27 18:06'),
        ),
    ]
