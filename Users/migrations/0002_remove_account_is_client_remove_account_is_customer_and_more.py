# Generated by Django 4.1.5 on 2023-02-02 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_client',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_link',
        ),
    ]