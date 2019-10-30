# Generated by Django 2.2.6 on 2019-10-30 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acc', '0006_ad_test_type0'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateTimeField()),
                ('is_done', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.All_Device')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rr', to='acc.record')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.Request')),
                ('totalcomment', models.ManyToManyField(related_name='rtotalcomment', to='acc.comment_cant_test')),
                ('tt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.ad_test_type0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]