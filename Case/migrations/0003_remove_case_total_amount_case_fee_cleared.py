# Generated by Django 4.1.5 on 2023-02-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0002_case_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='case',
            name='fee_cleared',
            field=models.BooleanField(default=False),
        ),
    ]
