# Generated by Django 4.0.6 on 2022-09-30 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0013_alter_receipt_receipt_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='proile_picture',
            new_name='profile_picture',
        ),
    ]