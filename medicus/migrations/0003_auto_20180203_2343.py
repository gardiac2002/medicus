# Generated by Django 2.0.2 on 2018-02-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicus', '0002_prepopulate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
