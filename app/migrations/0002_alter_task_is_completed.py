# Generated by Django 5.0 on 2023-12-31 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]