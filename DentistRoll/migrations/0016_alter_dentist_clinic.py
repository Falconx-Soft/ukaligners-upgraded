# Generated by Django 4.1.5 on 2023-03-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClinicRoll', '0001_initial'),
        ('DentistRoll', '0015_alter_dentist_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dentist',
            name='clinic',
            field=models.ManyToManyField(to='ClinicRoll.clinic'),
        ),
    ]