# Generated by Django 4.0.6 on 2023-07-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0013_survei'),
    ]

    operations = [
        migrations.AddField(
            model_name='survei',
            name='jabatan',
            field=models.CharField(choices=[('Pimpinan/kepala', 'Pimpinan/kepala'), ('Manajer', 'Manajer'), ('Supervisor', 'Supervisor'), ('Staf', 'Staf')], default='Staf', max_length=150),
        ),
    ]