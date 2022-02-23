# Generated by Django 4.0.2 on 2022-02-20 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid_document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(null=True, upload_to=pathlib.PureWindowsPath('G:/Minor Project/minor_project/static/assets/bid_documents'))),
            ],
        ),
        migrations.CreateModel(
            name='Job_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=512, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, max_length=255, null=True, upload_to=pathlib.PureWindowsPath('G:/Minor Project/minor_project/static/assets/profile_images'))),
                ('profile_title', models.TextField(null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('hourly_rate', models.PositiveIntegerField(blank=True, null=True)),
                ('hours_per_week', models.PositiveIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('field1', models.CharField(blank=True, max_length=255)),
                ('field2', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project_bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offered_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('offered_duration', models.PositiveIntegerField()),
                ('bid_description', models.TextField(null=True)),
                ('bid_status', models.CharField(choices=[('A', 'accepted'), ('P', 'pending'), ('R', 'rejected')], default='P', max_length=1)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Project_define',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=255)),
                ('project_description', models.TextField(null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('project_length', models.PositiveIntegerField(null=True)),
                ('budget_min', models.DecimalField(decimal_places=2, max_digits=7)),
                ('budget_max', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bid_deadline', models.DateTimeField()),
                ('projectFile', models.FileField(blank=True, null=True, upload_to='project_files/')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.profile')),
                ('job_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.job_category')),
            ],
        ),
        migrations.CreateModel(
            name='Project_document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(null=True, upload_to=pathlib.PureWindowsPath('G:/Minor Project/minor_project/static/assets/project_documents'))),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project_define')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='JobCategory',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='hide_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='project_define',
            name='skills',
            field=models.ManyToManyField(to='api.Skill'),
        ),
        migrations.AddField(
            model_name='project_bid',
            name='project_define',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project_define'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(to='api.Skill'),
        ),
        migrations.AddField(
            model_name='job_category',
            name='skills',
            field=models.ManyToManyField(to='api.Skill'),
        ),
        migrations.AddField(
            model_name='bid_document',
            name='project_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project_bid'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_description', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.project_define')),
                ('project_start_date', models.DateTimeField()),
                ('running_duration', models.PositiveIntegerField()),
                ('completion_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('C', 'completed'), ('R', 'running')], default='R', max_length=1)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.project')),
                ('reliability', models.PositiveSmallIntegerField()),
                ('punctuality', models.PositiveSmallIntegerField()),
                ('communication', models.PositiveSmallIntegerField()),
                ('quality_work', models.PositiveSmallIntegerField()),
                ('comment', models.TextField()),
                ('critic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_given', to='api.profile')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_received', to='api.profile')),
            ],
        ),
    ]
