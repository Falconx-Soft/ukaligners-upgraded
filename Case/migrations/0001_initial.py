# Generated by Django 4.1.5 on 2023-02-08 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DentistRoll', '0009_alter_dentist_clinic'),
        ('TechnicianRoll', '0001_initial'),
        ('SaloonRoll', '0001_initial'),
        ('PlannerRoll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('treatment_required', models.CharField(choices=[('full treatment', 'full treatment'), ('continuation', 'continuation'), ('refinement', 'refinement'), ('retainer', 'retainer')], max_length=100)),
                ('orthodontic_treatment_past', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=10, null=True)),
                ('section', models.CharField(blank=True, choices=[('both arches', 'both arches'), ('upper only', 'upper only'), ('lower only', 'lower only')], max_length=250, null=True)),
                ('treatment_type', models.CharField(blank=True, choices=[('essential', 'essential'), ('advance', 'advance'), ('comprehensive', 'comprehensive')], max_length=250, null=True)),
                ('upper_jaw', models.FileField(blank=True, null=True, upload_to='upper_jaws')),
                ('lower_jaw', models.FileField(blank=True, null=True, upload_to='lower_jaws')),
                ('rquest_collection', models.BooleanField(default=False)),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='new', max_length=250, null=True)),
                ('ortho_id', models.CharField(blank=True, max_length=255, null=True)),
                ('aligners_upper', models.IntegerField(blank=True, null=True)),
                ('aligners_lower', models.IntegerField(blank=True, null=True)),
                ('retainer_upper', models.IntegerField(blank=True, null=True)),
                ('retainer_lower', models.IntegerField(blank=True, null=True)),
                ('treatment_plan_upper', models.IntegerField(blank=True, null=True)),
                ('treatment_plan_lower', models.IntegerField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('progress', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DentistRoll.clinic')),
                ('dentist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='DentistRoll.dentist')),
                ('planner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PlannerRoll.planner')),
                ('saloon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SaloonRoll.saloon')),
                ('saloon_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='SaloonRoll.saloon_owner')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='TechnicianRoll.technician')),
            ],
            options={
                'verbose_name_plural': 'Cases',
            },
        ),
        migrations.CreateModel(
            name='Case_additional_videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos_uploaded')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Case.case')),
            ],
            options={
                'verbose_name_plural': 'Case additional Videos',
            },
        ),
        migrations.CreateModel(
            name='Case_additional_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Additional_images')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Case.case')),
            ],
            options={
                'verbose_name_plural': 'Case additional images',
            },
        ),
    ]