# Generated by Django 2.2.6 on 2019-11-13 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acc', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='licence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateTimeField()),
                ('totalcomment', models.TextField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.All_Device')),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me1licence', to='report.licence')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rr', to='report.record')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.Request')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.ad_az_Status')),
                ('tt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.ad_test_type0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'سابقه گزارشات',
            },
        ),
    ]
