# Generated by Django 4.0.6 on 2022-07-22 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_addbooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addbooking',
            old_name='vehicleType',
            new_name='type',
        ),
    ]
