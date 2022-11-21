# Generated by Django 4.1.2 on 2022-11-20 20:37

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_invoice_urn_alter_booking_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForLessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_lessons', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1, message='Number of lessons must be greater than 1!')])),
                ('days_between_lessons', models.IntegerField(default=7, validators=[django.core.validators.MinValueValidator(1, message='Number of days between lessons must be greater than 1!')])),
                ('lesson_duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('other_info', models.CharField(blank=True, max_length=500)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
