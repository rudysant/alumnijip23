# Generated by Django 4.0.6 on 2023-07-14 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0012_testdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survei',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('tempat_kerja', models.CharField(choices=[('Perpustakaan', 'Perpustakaan'), ('Non-perpustakaan', 'Non-perpustakaan')], default='Perpustakaan', max_length=150)),
                ('jenis_instansi', models.CharField(choices=[('Pemerintahan', 'Pemerintahan'), ('NGO', 'NGO'), ('Komersial', 'Komersial')], default='Pemerintahan', max_length=150)),
            ],
        ),
    ]
