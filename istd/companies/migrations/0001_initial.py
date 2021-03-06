# Generated by Django 2.2.2 on 2019-06-08 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название компании')),
                ('description', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='companies/', verbose_name='Картинка компании')),
                ('date_created', models.DateField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name_plural': 'Компании',
                'verbose_name': 'Компания',
            },
        ),
        migrations.CreateModel(
            name='UsersInCompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(1, 'admin'), (2, 'moderator'), (3, 'member')], default='3', max_length=20)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.Company')),
            ],
        ),
    ]
