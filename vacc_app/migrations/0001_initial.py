# Generated by Django 3.2.9 on 2021-12-01 05:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vac_Centers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=100)),
                ('vac_type', models.CharField(choices=[('P', 'Pfizer'), ('M', 'Moderna')], max_length=100)),
                ('postal_code', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999)])),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField()),
                ('time_slots', models.CharField(choices=[('9am', '9am'), ('10am', '10am'), ('11am', '11am'), ('12am', '12am'), ('1pm', '1pm'), ('2pm', '2pm'), ('3pm', '3pm'), ('4pm', '4pm')], max_length=100)),
                ('first_or_second', models.CharField(choices=[('First', 'First jab'), ('Second', 'Second jab')], max_length=100)),
                ('person_name', models.CharField(max_length=100)),
                ('person_nric', models.CharField(max_length=4)),
                ('vac_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.vac_centers')),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jab_done', models.CharField(choices=[('None', 'None'), ('First done', 'First done'), ('Second done', 'Second done')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
