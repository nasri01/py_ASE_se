# Generated by Django 2.2.6 on 2019-12-27 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20191224_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electrocauter_1',
            name='s0_e16_comment',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='ec1s0e16comment', to='acc.comment'),
        ),
        migrations.AlterField(
            model_name='ventilator_1',
            name='s16_e5',
            field=models.FloatField(),
        ),
    ]