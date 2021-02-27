# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-17 11:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0004_auto_20191114_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical_script2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name='الرقم الطبى ')),
                ('auth_doc', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=120, verbose_name='طبيب العيادة ')),
                ('medic1_name', models.CharField(max_length=120, verbose_name='علاج 1')),
                ('medic2_name', models.CharField(max_length=120, verbose_name='2 علاج ')),
                ('medic3_name', models.CharField(max_length=120, verbose_name='3 علاج ')),
                ('medic4_name', models.CharField(max_length=120, verbose_name='4  علاج')),
                ('medic5_name', models.CharField(max_length=120, verbose_name='علاج 5  ')),
                ('medic6_name', models.CharField(max_length=120, verbose_name='6 علاج ')),
                ('medic7_name', models.CharField(max_length=120, verbose_name='علاج 7  ')),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=120, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthly_medical_script1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name='الرقم الطبى ')),
                ('auth_doc', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=120, verbose_name='طبيب العيادة ')),
                ('medic1_name', models.CharField(max_length=120, verbose_name='علاج 1')),
                ('medic2_name', models.CharField(max_length=120, verbose_name='2 علاج ')),
                ('medic3_name', models.CharField(max_length=120, verbose_name='3 علاج ')),
                ('medic4_name', models.CharField(max_length=120, verbose_name='4  علاج')),
                ('medic5_name', models.CharField(max_length=120, verbose_name='علاج 5  ')),
                ('medic6_name', models.CharField(max_length=120, verbose_name='6 علاج ')),
                ('medic7_name', models.CharField(max_length=120, verbose_name='علاج 7  ')),
                ('medic8_name', models.CharField(max_length=120, verbose_name='علاج 8')),
                ('medic9_name', models.CharField(max_length=120, verbose_name='9 علاج ')),
                ('medic10_name', models.CharField(max_length=120, verbose_name='10 علاج ')),
                ('medic11_name', models.CharField(max_length=120, verbose_name='11  علاج')),
                ('medic12_name', models.CharField(max_length=120, verbose_name='علاج 12  ')),
                ('medic13_name', models.CharField(max_length=120, verbose_name='13 علاج ')),
                ('medic14_name', models.CharField(max_length=120, verbose_name='علاج 14  ')),
                ('medic15_name', models.CharField(max_length=120, verbose_name='علاج 15')),
                ('medic16_name', models.CharField(max_length=120, verbose_name='16 علاج ')),
                ('medic17_name', models.CharField(max_length=120, verbose_name='17 علاج ')),
                ('medic18_name', models.CharField(max_length=120, verbose_name='18  علاج')),
                ('medic19_name', models.CharField(max_length=120, verbose_name='علاج 19  ')),
                ('medic20_name', models.CharField(max_length=120, verbose_name='20 علاج ')),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=120, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='monthly_medical_script2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name='الرقم الطبى ')),
                ('auth_doc', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=120, verbose_name='طبيب العيادة ')),
                ('medic1_name', models.CharField(max_length=120, verbose_name='علاج 1')),
                ('medic2_name', models.CharField(max_length=120, verbose_name='2 علاج ')),
                ('medic3_name', models.CharField(max_length=120, verbose_name='3 علاج ')),
                ('medic4_name', models.CharField(max_length=120, verbose_name='4  علاج')),
                ('medic5_name', models.CharField(max_length=120, verbose_name='علاج 5  ')),
                ('medic6_name', models.CharField(max_length=120, verbose_name='6 علاج ')),
                ('medic7_name', models.CharField(max_length=120, verbose_name='علاج 7  ')),
                ('medic8_name', models.CharField(max_length=120, verbose_name='علاج 8')),
                ('medic9_name', models.CharField(max_length=120, verbose_name='9 علاج ')),
                ('medic10_name', models.CharField(max_length=120, verbose_name='10 علاج ')),
                ('medic11_name', models.CharField(max_length=120, verbose_name='11  علاج')),
                ('medic12_name', models.CharField(max_length=120, verbose_name='علاج 12  ')),
                ('medic13_name', models.CharField(max_length=120, verbose_name='13 علاج ')),
                ('medic14_name', models.CharField(max_length=120, verbose_name='علاج 14  ')),
                ('medic15_name', models.CharField(max_length=120, verbose_name='علاج 15')),
                ('medic16_name', models.CharField(max_length=120, verbose_name='16 علاج ')),
                ('medic17_name', models.CharField(max_length=120, verbose_name='17 علاج ')),
                ('medic18_name', models.CharField(max_length=120, verbose_name='18  علاج')),
                ('medic19_name', models.CharField(max_length=120, verbose_name='علاج 19  ')),
                ('medic20_name', models.CharField(max_length=120, verbose_name='20 علاج ')),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=120, null=True)),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='medical_script',
            new_name='medical_script1',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_addr',
            field=models.CharField(max_length=120, verbose_name='عنوان المستشفى '),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(max_length=120, verbose_name='اسم المستشفى '),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='lab_name',
            field=models.CharField(max_length=120, verbose_name='اسم المعمل '),
        ),
    ]
