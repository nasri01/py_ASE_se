# Generated by Django 2.2.6 on 2019-10-31 02:49

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
                ('is_done', models.BooleanField(default=False)),
                ('aed_totalcomment', models.ManyToManyField(related_name='raedtotalcomment', to='acc.qualitive_comment_aed')),
                ('anesthesia_machine_totalcomment', models.ManyToManyField(related_name='ramtotalcomment', to='acc.qualitive_comment_anesthesia_machine')),
                ('cant_test_totalcomment', models.ManyToManyField(related_name='rcttotalcomment', to='acc.qualitive_comment_cant_test')),
                ('defibrilator_totalcomment', models.ManyToManyField(related_name='rdetotalcomment', to='acc.qualitive_comment_defibrilator')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.All_Device')),
                ('ecg_totalcomment', models.ManyToManyField(related_name='recgtotalcomment', to='acc.qualitive_comment_ecg')),
                ('electrocauter_totalcomment', models.ManyToManyField(related_name='rectotalcomment', to='acc.qualitive_comment_electrocouter')),
                ('flowmeter_totalcomment', models.ManyToManyField(related_name='rfmtotalcomment', to='acc.qualitive_comment_flowmeter')),
                ('infusion_pump_totalcomment', models.ManyToManyField(related_name='riptotalcomment', to='acc.qualitive_comment_infusion_pump')),
                ('licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me1licence', to='report.licence')),
                ('monitor_ecg_totalcomment', models.ManyToManyField(related_name='rmetotalcomment', to='acc.qualitive_comment_monitor_ecg')),
                ('monitor_nibp_totalcomment', models.ManyToManyField(related_name='rmntotalcomment', to='acc.qualitive_comment_monitor_nibp')),
                ('monitor_safety_totalcomment', models.ManyToManyField(related_name='rmsafetotalcomment', to='acc.qualitive_comment_monitor_safety')),
                ('monitor_spo2_totalcomment', models.ManyToManyField(related_name='rmspo2totalcomment', to='acc.qualitive_comment_monitor_spo2')),
                ('monometer_totalcomment', models.ManyToManyField(related_name='rmmtotalcomment', to='acc.qualitive_comment_monometer')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rr', to='report.record')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.Request')),
                ('spo2_totalcomment', models.ManyToManyField(related_name='rspo2totalcomment', to='acc.qualitive_comment_spo2')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.ad_az_Status')),
                ('suction_totalcomment', models.ManyToManyField(related_name='rsutotalcomment', to='acc.qualitive_comment_suction')),
                ('syringe_pump_totalcomment', models.ManyToManyField(related_name='rsptotalcomment', to='acc.qualitive_comment_syringe_pump')),
                ('tt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.ad_test_type0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('ventilator_totalcomment', models.ManyToManyField(related_name='rvetotalcomment', to='acc.qualitive_comment_ventilator')),
            ],
        ),
    ]