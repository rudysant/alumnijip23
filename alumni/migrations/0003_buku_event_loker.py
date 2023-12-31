# Generated by Django 4.0.6 on 2023-07-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_profile_angkatan_profile_lulusan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('judul', models.CharField(max_length=150)),
                ('penerbit', models.CharField(max_length=150)),
                ('pengarang', models.CharField(max_length=150)),
                ('deskripsi', models.TextField()),
                ('cover', models.ImageField(default='logounpad.jpg', upload_to='cover')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('acara', models.CharField(max_length=150)),
                ('tanggal', models.DateField()),
                ('tempat', models.CharField(max_length=150)),
                ('deskripsi', models.TextField()),
                ('foto', models.ImageField(default='logounpad.jpg', upload_to='event')),
            ],
        ),
        migrations.CreateModel(
            name='Loker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('posisi', models.CharField(max_length=150)),
                ('instansi', models.CharField(max_length=150)),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]
