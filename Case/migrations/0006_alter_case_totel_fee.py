# Generated by Django 4.1.5 on 2023-02-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0005_case_manager_paid_case_planner_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='totel_fee',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
