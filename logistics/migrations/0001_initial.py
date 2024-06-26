# Generated by Django 5.0.4 on 2024-05-08 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(upload_to='company/')),
                ('address', models.CharField(max_length=255)),
                ('address_en', models.CharField(max_length=255, null=True)),
                ('address_uz', models.CharField(max_length=255, null=True)),
                ('address_ru', models.CharField(max_length=255, null=True)),
                ('inn', models.CharField(max_length=255)),
                ('inn_en', models.CharField(max_length=255, null=True)),
                ('inn_uz', models.CharField(max_length=255, null=True)),
                ('inn_ru', models.CharField(max_length=255, null=True)),
                ('kpp', models.CharField(max_length=255)),
                ('kpp_en', models.CharField(max_length=255, null=True)),
                ('kpp_uz', models.CharField(max_length=255, null=True)),
                ('kpp_ru', models.CharField(max_length=255, null=True)),
                ('okpo', models.CharField(max_length=255)),
                ('okpo_en', models.CharField(max_length=255, null=True)),
                ('okpo_uz', models.CharField(max_length=255, null=True)),
                ('okpo_ru', models.CharField(max_length=255, null=True)),
                ('bank', models.CharField(max_length=255)),
                ('bank_en', models.CharField(max_length=255, null=True)),
                ('bank_uz', models.CharField(max_length=255, null=True)),
                ('bank_ru', models.CharField(max_length=255, null=True)),
                ('account_number1', models.FloatField()),
                ('account_number2', models.FloatField()),
                ('account_number3', models.FloatField()),
                ('kor_shot', models.CharField(max_length=255)),
                ('kor_shot_en', models.CharField(max_length=255, null=True)),
                ('kor_shot_uz', models.CharField(max_length=255, null=True)),
                ('kor_shot_ru', models.CharField(max_length=255, null=True)),
                ('bike', models.CharField(max_length=255)),
                ('bike_en', models.CharField(max_length=255, null=True)),
                ('bike_uz', models.CharField(max_length=255, null=True)),
                ('bike_ru', models.CharField(max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='contract_title', max_length=255)),
                ('title_en', models.CharField(default='contract_title', max_length=255, null=True)),
                ('title_uz', models.CharField(default='contract_title', max_length=255, null=True)),
                ('title_ru', models.CharField(default='contract_title', max_length=255, null=True)),
                ('akt', models.FileField(upload_to='contract/')),
                ('invoice', models.FileField(upload_to='contract/')),
                ('zayavka', models.FileField(upload_to='contract/')),
                ('cmr', models.FileField(upload_to='contract/')),
                ('contract_number', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
                ('auto_number', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='logistics.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
