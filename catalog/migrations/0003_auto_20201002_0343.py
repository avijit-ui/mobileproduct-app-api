# Generated by Django 3.1.2 on 2020-10-01 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_mobilelist_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MobileList',
            new_name='Mobile',
        ),
    ]
