# Generated by Django 4.0.6 on 2022-10-28 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_app', '0007_customuser_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_super_user',
            new_name='is_superuser',
        ),
    ]