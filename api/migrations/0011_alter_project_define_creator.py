# Generated by Django 4.0.2 on 2022-03-07 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_define',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.profile'),
        ),
    ]