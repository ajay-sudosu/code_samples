# Generated by Django 4.0.6 on 2022-10-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_app', '0006_customuser_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
