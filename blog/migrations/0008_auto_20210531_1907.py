# Generated by Django 3.1.5 on 2021-05-31 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210531_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textmodel',
            old_name='CreatedDate',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='textmodel',
            old_name='editingDate',
            new_name='editing_date',
        ),
    ]
