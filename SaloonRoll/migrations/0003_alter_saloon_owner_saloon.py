# Generated by Django 4.1.5 on 2023-03-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SaloonRoll', '0002_alter_saloon_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saloon_owner',
            name='saloon',
            field=models.ManyToManyField(to='SaloonRoll.saloon'),
        ),
    ]
