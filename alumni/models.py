from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    angkatan = models.IntegerField(null=True)
    lulusan = models.IntegerField(null=True)
    avatar = models.ImageField(default='logounpad.jpg', upload_to='photo')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acara = models.CharField(max_length =150)
    tanggal = models.DateField()
    tempat = models.CharField(max_length =150)
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='event', blank=True)

    def __str__(self):
        return self.acara

    class Meta:
        permissions = [
            ("view_mypage", "Can view My Page"),
        ]

class Buku(models.Model):
    user = models.CharField(max_length =150)
    judul = models.CharField(max_length =150)
    penerbit = models.CharField(max_length =150)
    pengarang = models.CharField(max_length =150)
    deskripsi = models.TextField()
    cover = models.ImageField(default='logounpad.jpg', upload_to='cover')

    def __str__(self):
        return self.judul

class Loker(models.Model):
    user = models.CharField(max_length =150)
    posisi = models.CharField(max_length =150)
    batas = models.DateField(null=True)
    instansi = models.CharField(max_length =150)
    deskripsi = models.TextField()

class Artikel(models.Model):
    user = models.CharField(max_length =150)
    judul = models.CharField(max_length =150)
    artikel = models.TextField()

    def __str__(self):
        return self.judul

class Survei(models.Model):
    user = models.CharField(max_length = 50)
    tempat_kerja = models.CharField(max_length =150, choices=[
        ('Perpustakaan','Perpustakaan'),
        ('Non-perpustakaan','Non-perpustakaan'),
        ], default='Perpustakaan')


    jenis_instansi = models.CharField(max_length =150, choices=[
        ('Pemerintahan','Pemerintahan'),
        ('NGO','NGO'),
        ('Komersial','Komersial'),
        ], default='Pemerintahan')

    jabatan = models.CharField(max_length =150, choices=[
        ('Pimpinan/kepala','Pimpinan/kepala'),
        ('Manajer','Manajer'),
        ('Supervisor','Supervisor'),
        ('Staf','Staf'),
        ], default='Staf')



    def __str__(self):
        return self.user





class TestDB(models.Model):
    user = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.user


class TestData(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()

    def __str__(self):
        return self.name