# Generated by Django 2.2.6 on 2020-02-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20191228_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anesthesia_machine_1',
            name='s1_res',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='defibrilator_1',
            name='s1_res',
            field=models.FloatField(),
        ),
    ]
