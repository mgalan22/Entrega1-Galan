# Generated by Django 4.1 on 2022-09-03 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_categories',
            old_name='cant_post',
            new_name='post_qty',
        ),
    ]
