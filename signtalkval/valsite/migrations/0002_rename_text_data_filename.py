# Generated by Django 4.2.2 on 2023-06-28 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='text',
            new_name='filename',
        ),
    ]
