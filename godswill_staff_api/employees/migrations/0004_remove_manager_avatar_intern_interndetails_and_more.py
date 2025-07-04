# Generated by Django 5.2.3 on 2025-06-28 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_manager_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='avatar',
        ),
        migrations.AddField(
            model_name='intern',
            name='internDetails',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intern_details', to='employees.staffbase'),
        ),
        migrations.AddField(
            model_name='manager',
            name='staffDetails',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_details', to='employees.staffbase'),
        ),
    ]
