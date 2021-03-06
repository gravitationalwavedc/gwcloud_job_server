# Generated by Django 3.0.4 on 2020-05-17 22:34

from django.db import migrations, models
from django.utils import timezone


def migrate_bilby_jobs(apps, schema_editor):
    Job = apps.get_model("jobserver", "Job")

    # Iterate over all bilby jobs
    for job in Job.objects.filter(application='bilby'):
        job.application = 'bilbyui'
        job.save()


class Migration(migrations.Migration):
    dependencies = [
        ('jobserver', '0015_job_application'),
    ]

    operations = [
        migrations.RunPython(migrate_bilby_jobs),
    ]
