# Generated by Django 4.1 on 2022-09-29 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_posts_content_alter_posts_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.RenameModel(
            old_name='Post_categories',
            new_name='Post_category',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
