# Generated by Django 3.1.4 on 2020-12-27 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='active',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='begin_date',
        ),
    ]
