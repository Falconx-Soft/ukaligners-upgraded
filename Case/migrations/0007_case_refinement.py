# Generated by Django 4.1.5 on 2023-03-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Case', '0006_alter_case_totel_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='refinement',
            field=models.IntegerField(default=1),
        ),
    ]
