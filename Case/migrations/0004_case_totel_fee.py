# Generated by Django 4.1.5 on 2023-02-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0003_remove_case_total_amount_case_fee_cleared'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='totel_fee',
            field=models.FloatField(default=0.0),
        ),
    ]
