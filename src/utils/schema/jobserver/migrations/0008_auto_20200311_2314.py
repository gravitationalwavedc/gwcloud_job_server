# Generated by Django 3.0.4 on 2020-03-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobserver', '0007_auto_20200311_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedownload',
            name='uuid',
            field=models.CharField(db_index=True, max_length=36, unique=True),
        ),
    ]