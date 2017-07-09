# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('work', models.CharField(max_length=50, verbose_name='Специализация')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_message', models.EmailField(max_length=50, verbose_name='Отправитель')),
                ('to_message', models.EmailField(max_length=50, verbose_name='Получатель')),
                ('topic', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.CharField(max_length=300, verbose_name='Сообщение')),
            ],
        ),
    ]
