# Generated by Django 4.1.4 on 2023-01-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
