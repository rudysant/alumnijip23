# Generated by Django 4.0.6 on 2023-07-07 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0007_alter_event_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.CharField(default='{{user.username}}', max_length=150),
        ),
    ]
