# Generated by Django 2.2.10 on 2020-03-07 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdAccStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'سلسله مراتب حسابها',
            },
        ),
        migrations.CreateModel(
            name='AdAzStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'وضعیت های آزمایش',
            },
        ),
        migrations.CreateModel(
            name='AdExcelArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arg', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'آرگومان اکسل',
            },
        ),
        migrations.CreateModel(
            name='AdReqStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'وضعیت های درخواست',
            },
        ),
        migrations.CreateModel(
            name='AdTestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'کلاس تست',
            },
        ),
        migrations.CreateModel(
            name='AdTestType0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'نوع آزمایش',
            },
        ),
        migrations.CreateModel(
            name='AdTestType1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'کلاس تست 2',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('eng_name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'شهر ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'توضیحات',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('en_name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'شرکت های سازنده',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'کشور ها',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'نوع دستگاه ها',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.City')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '2_بیمارستان ها',
            },
        ),
        migrations.CreateModel(
            name='Licence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'شماره گواهی',
            },
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'پارامتر ها',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'شماره رکورد',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('eng_name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'بخش های بیمارستان',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='signature/')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.AdAccStatus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1_مشخصات کاربران',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('eng_name', models.TextField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Country')),
            ],
            options={
                'verbose_name_plural': 'استان ها',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateField()),
                ('number', models.IntegerField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Hospital')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acc.AdReqStatus')),
            ],
            options={
                'verbose_name_plural': '5_لیست درخواست ها',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Company')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.DeviceType')),
            ],
            options={
                'verbose_name_plural': 'لیست دستگاه',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.State'),
        ),
        migrations.CreateModel(
            name='CalDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('serial', models.CharField(max_length=30)),
                ('calibration_date', models.DateField()),
                ('calibration_Expire_date', models.DateField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Company')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.DeviceType')),
            ],
            options={
                'verbose_name_plural': '4_دستگاه های کنترل کیفی',
            },
        ),
        migrations.CreateModel(
            name='AllDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.TextField(blank=True, null=True)),
                ('property_number', models.IntegerField(blank=True, null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Hospital')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Device')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acc.Section')),
            ],
            options={
                'verbose_name_plural': '3_دستگاه های ثبت شده',
            },
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.Company')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acc.DeviceType')),
            ],
            options={
                'verbose_name_plural': 'لوازم جانبی',
            },
        ),
    ]
