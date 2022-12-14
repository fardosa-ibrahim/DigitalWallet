# Generated by Django 4.0.6 on 2022-08-19 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0008_thirdparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('status', models.BooleanField(null=True)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Notification_recipient', to='walletapp.customer')),
            ],
        ),
    ]
