# Generated by Django 2.2.6 on 2019-10-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acc_status',
            options={'verbose_name_plural': 'accStatus'},
        ),
        migrations.AddField(
            model_name='company',
            name='en_name',
            field=models.TextField(default='ssa'),
            preserve_default=False,
        ),
    ]
