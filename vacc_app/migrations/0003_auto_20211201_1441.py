# Generated by Django 3.2.9 on 2021-12-01 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacc_app', '0002_auto_20211201_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='person_last4nric',
        ),
        migrations.RemoveField(
            model_name='slots',
            name='person_last4nric',
        ),
        migrations.AddField(
            model_name='slots',
            name='person_nric',
            field=models.CharField(max_length=4, null=True),
        ),
    ]