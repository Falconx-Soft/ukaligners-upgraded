# Generated by Django 4.1.5 on 2023-03-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminRoll', '0002_alter_fee_fee_aligner_alter_fee_fee_comprehensive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='fee_mouthguard',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='fee',
            name='fee_replacement',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AddField(
            model_name='fee',
            name='fee_smile_design',
            field=models.IntegerField(default=0.0),
        ),
    ]
