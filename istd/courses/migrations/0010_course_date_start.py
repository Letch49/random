# Generated by Django 2.2.2 on 2019-06-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_subscribetocourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_start',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время начала курса'),
        ),
    ]
