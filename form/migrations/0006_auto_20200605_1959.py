# Generated by Django 2.2.10 on 2020-06-05 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20200410_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecg_1',
            name='s6_e3_comment',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, related_name='e1s6e3comment', to='acc.Comment'),
        ),
        migrations.AlterField(
            model_name='monitorecg_1',
            name='s7_e4_damp',
            field=models.FloatField(default=200),
        ),
        migrations.AlterField(
            model_name='monitorecg_1',
            name='s7_e5_damp',
            field=models.FloatField(default=200),
        ),
    ]