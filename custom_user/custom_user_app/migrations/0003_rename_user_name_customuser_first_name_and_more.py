# Generated by Django 4.0.6 on 2022-10-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_app', '0002_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
