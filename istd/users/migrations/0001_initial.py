# Generated by Django 2.2.2 on 2019-06-08 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Имя пользователя')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')),
                ('is_staff', models.BooleanField(default=False, verbose_name='сотрудник?')),
                ('is_confirm', models.BooleanField(default=False, verbose_name='подтверждённый юзер')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'пользователи',
                'verbose_name': 'пользователь',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Возраст пользователя')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('avatar', models.ImageField(upload_to='avatars/', verbose_name='Аватар')),
                ('about', models.TextField(verbose_name='О себе')),
                ('sex', models.IntegerField(choices=[('M', 'Мужской'), ('F', 'Женский')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Профили пользователя',
                'verbose_name': 'Профиль пользователя',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
            ],
            options={
                'indexes': [],
                'constraints': [],
                'proxy': True,
                'verbose_name_plural': 'Профили пользователей',
                'verbose_name': 'Профиль пользователя',
            },
            bases=('users.userprofile',),
        ),
    ]
