from django.urls import path
from . import views
from .views import RegisterView, CustomLoginView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('alumni/', views.alumni, name='alumni'),
#    path('artikel/', views.artikel, name='artikel'),
    path('alumni/detail_alumni/<int:id>/', views.detail_alumni, name='detail_alumni'),
    path('alumni/detail_angkatan/<int:angkatan>/', views.detail_angkatan, name='detail_angkatan'),
    path('list_berita/detail_berita/<int:id>/', views.detail_berita, name='detail_berita'),
    path('berita/', views.berita, name='berita'),
    path('list_berita/', views.list_berita, name='list_berita'),
    path('resensi/', views.resensi, name='resensi'),
    path('list_resensi/', views.list_resensi, name='list_resensi'),
    path('list_resensi/detail_resensi/<int:id>/', views.detail_resensi, name='detail_resensi'),
    path('loker/', views.loker, name='loker'),
    path('list_loker/', views.list_loker, name='list_loker'),
    path('list_loker/detail_loker/<int:id>/', views.detail_loker, name='detail_loker'),

    path('testpagination/', views.testpagination, name='testpagination'),
    path('isi_survei/', views.isi_survei, name='isi_survei'),
    path('artikel/', views.artikel, name='artikel'),
    path('list_artikel/', views.list_artikel, name='list_artikel'),
    path('list_artikel/detail_artikel/<int:id>/', views.detail_artikel, name='detail_artikel'),

    path('alumni/pekerjaan-chart/', views.pekerjaan_chart, name='pekerjaan-chart'),
    path('alumni/institusi-chart/', views.institusi_chart, name='institusi-chart'),
    path('alumni/jabatan-chart/', views.jabatan_chart, name='jabatan-chart'),
]