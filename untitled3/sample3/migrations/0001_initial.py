# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 10:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sample3.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('address1', models.CharField(blank=True, max_length=100, null=True)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True, validators=[sample3.validators.validate_city])),
                ('state', models.CharField(blank=True, max_length=20, null=True, validators=[sample3.validators.validate_state])),
                ('landmark', models.CharField(blank=True, max_length=20, null=True, validators=[sample3.validators.validate_landmark])),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=20, validators=[sample3.validators.validate_mobile_number])),
                ('phone_number', models.CharField(max_length=20, validators=[sample3.validators.validate_phone_number])),
                ('email_id', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=11)),
                ('iam_name', models.CharField(choices=[('agent', 'AGENT'), ('buyer', 'BUYER'), ('owner', 'OWNER'), ('builder', 'BUILDER')], default='agent', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('contactinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='sample3.ContactInfo')),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20, validators=[sample3.validators.validate_first_name])),
                ('last_name', models.CharField(max_length=20, validators=[sample3.validators.validate_last_name])),
            ],
            bases=('sample3.contactinfo',),
        ),
        migrations.AddField(
            model_name='address',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample3.Customer'),
        ),
    ]
