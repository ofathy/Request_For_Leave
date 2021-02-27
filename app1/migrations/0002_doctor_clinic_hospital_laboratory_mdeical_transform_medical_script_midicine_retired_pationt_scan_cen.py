# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-10 17:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=120, verbose_name=' اسم الطبيب  ')),
                ('clinic_addr', models.CharField(max_length=120, verbose_name=' العنوان ')),
                ('clinic_spesilization', models.CharField(max_length=120, verbose_name=' التخصص ')),
                ('clinic_price', models.CharField(max_length=120, verbose_name='سعر الكشف')),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('hospital_addr', models.CharField(max_length=120, verbose_name='اسم المريض ')),
            ],
        ),
        migrations.CreateModel(
            name='laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
            ],
        ),
        migrations.CreateModel(
            name='mdeical_transform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('auth_doc', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=120, verbose_name='طبيب العيادة ')),
                ('to_clinic', models.CharField(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, verbose_name='العيادة التابعة')),
                ('to_lab', models.CharField(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, verbose_name='العيادة التابعة')),
                ('followed_clinic', models.CharField(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, verbose_name='العيادة التابعة')),
                ('to_hospital', models.ForeignKey(max_length=120, on_delete=django.db.models.deletion.CASCADE, to='app1.hospital', verbose_name='العيادة التابعة')),
            ],
        ),
        migrations.CreateModel(
            name='medical_script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('auth_doc', models.CharField(choices=[('', ''), ('', ''), ('', ''), ('', ''), ('', '')], max_length=120, verbose_name='طبيب العيادة ')),
                ('medic1_name', models.CharField(max_length=120, verbose_name='علاج')),
                ('medic2_name', models.CharField(max_length=120, verbose_name=' علاج ')),
                ('medic3_name', models.CharField(max_length=120, verbose_name=' علاج ')),
                ('medic4_name', models.CharField(max_length=120, verbose_name='  علاج')),
                ('medic5_name', models.CharField(max_length=120, verbose_name='علاج  ')),
                ('medic6_name', models.CharField(max_length=120, verbose_name=' علاج ')),
                ('medic7_name', models.CharField(max_length=120, verbose_name='علاج  ')),
            ],
        ),
        migrations.CreateModel(
            name='midicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('midicine_name', models.CharField(max_length=120, verbose_name='اسم الدواء ')),
                ('midicine_price', models.CharField(max_length=120, verbose_name='السعر')),
            ],
        ),
        migrations.CreateModel(
            name='retired_pationt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('patient_age', models.CharField(max_length=120, verbose_name='سن المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name=' الرقم الطبى ')),
                ('notes_number', models.CharField(max_length=120, verbose_name='رقم الدفتر ')),
                ('followed_clinic', models.CharField(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, verbose_name='العيادة التابعة')),
            ],
        ),
        migrations.CreateModel(
            name='scan_center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='working_pationt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض ')),
                ('patient_age', models.CharField(max_length=120, verbose_name='سن المريض ')),
                ('medical_number', models.CharField(max_length=120, verbose_name=' الرقم الطبى ')),
                ('notes_number', models.CharField(max_length=120, verbose_name='رقم الدفتر ')),
                ('followed_clinic', models.CharField(choices=[('جاردن سيتى', 'جاردن سيتى'), ('الفوالة', 'الفوالة'), ('المهندسيين', 'المهندسيين')], max_length=120, verbose_name='العيادة التابعة')),
            ],
        ),
    ]
