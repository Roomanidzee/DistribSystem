# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 15:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userroles.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', userroles.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cooperator',
            fields=[
                ('abstractperson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='userroles.AbstractPerson')),
                ('work', models.CharField(max_length=50, verbose_name='Специализация')),
                ('user', userroles.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='cooperator', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            bases=('userroles.abstractperson',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('abstractperson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='userroles.AbstractPerson')),
                ('education_course', models.CharField(max_length=100, verbose_name='Предмет')),
                ('user', userroles.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='professor', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            bases=('userroles.abstractperson',),
        ),
        migrations.CreateModel(
            name='ScientificDirector',
            fields=[
                ('abstractperson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='userroles.AbstractPerson')),
                ('education_course', models.CharField(max_length=100, verbose_name='Предмет')),
                ('user', userroles.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='scientific_director', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            bases=('userroles.abstractperson',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('abstractperson_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='userroles.AbstractPerson')),
                ('group', models.CharField(max_length=10, verbose_name='Группа студента')),
                ('course', models.CharField(max_length=10, verbose_name='Курс студента')),
                ('user', userroles.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            bases=('userroles.abstractperson',),
        ),
    ]
