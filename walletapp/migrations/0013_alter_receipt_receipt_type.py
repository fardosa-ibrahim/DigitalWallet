# Generated by Django 4.0.6 on 2022-08-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0012_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='receipt_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]