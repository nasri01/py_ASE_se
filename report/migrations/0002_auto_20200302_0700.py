# Generated by Django 2.2.10 on 2020-03-02 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='licence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rl', to='acc.Licence'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rr', to='acc.Record'),
        ),
    ]