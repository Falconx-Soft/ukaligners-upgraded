# Generated by Django 4.1.5 on 2023-02-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_planner', models.BooleanField(default=False)),
                ('is_technician', models.BooleanField(default=False)),
                ('is_dentist', models.BooleanField(default=False)),
                ('is_salon', models.BooleanField(default=False)),
                ('is_individual', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
                ('is_client', models.BooleanField(default=False)),
                ('is_link', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]