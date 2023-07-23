from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View
from .forms import RegisterForm, LoginForm, EventAlumni, BukuAlumni, LokerAlumni, IsiSurvei, ArtikelAlumni
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
#from .tables import PaginatedTable

from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User
from .models import Profile, Event, Buku, Loker, Survei, Artikel


def home(request):
    total_alumni = Profile.objects.count()
    baru_daftar = User.objects.latest('id')
    nama_baru_daftar = Profile.objects.get(user=baru_daftar)
    angkatan = Profile.objects.values('angkatan').annotate(angkatancount=Count('angkatan'))
    baru_loker = Loker.objects.latest('id')
    typekerjaan = Survei.objects.values('tempat_kerja').annotate(typepekerjaancount=Count('tempat_kerja'))
    typekantor = Survei.objects.values('jenis_instansi').annotate(typekantorcount=Count('jenis_instansi'))
    jabatan = Survei.objects.values('jabatan').annotate(jabatancount=Count('jabatan'))


    context = {
        'total_alumni' : total_alumni,
        'angkatan' : angkatan,
        'baru_daftar' : baru_daftar,
        'nama_baru_daftar' : nama_baru_daftar,
        'baru_loker' : baru_loker,
        'typekerjaan' : typekerjaan,
        'typekantor' : typekantor,
        'jabatan' : jabatan,
        }

    return render(request,'home.html', context)

@login_required
def berita(request):
    if request.method == 'POST':
        form = EventAlumni(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = EventAlumni(request.user)
    return render(request,'berita.html', {'form': form})

@login_required
def resensi(request):
    if request.method == 'POST':
        form = BukuAlumni(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = BukuAlumni(request.user)
    return render(request,'resensi.html', {'form': form})

@login_required
def loker(request):
    if request.method == 'POST':
        form = LokerAlumni(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = LokerAlumni(request.user)
    return render(request,'lokeralumni.html', {'form': form})

@login_required
def artikel(request):
    if request.method == 'POST':
        form = ArtikelAlumni(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = ArtikelAlumni(request.user)
    return render(request,'artikelalumni.html', {'form': form})


@login_required
def isi_survei(request):
    if request.method == 'POST':
        form = IsiSurvei(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
    else:
        form = IsiSurvei(request.user)
    return render(request,'survei.html', {'form': form})

def list_resensi(request):
    resensi = Buku.objects.all()
    context = {'resensi' : resensi}

    return render(request,'list_resensi.html', context)

#@permission_required('alumni.view_mypage')
def list_berita(request):
    berita = Event.objects.all().order_by('-tanggal')
    context = {'berita' : berita}

    return render(request,'list_berita.html', context)

def list_loker(request):
    loker = Loker.objects.all().order_by('-batas')
    context = {'loker' : loker}

    return render(request,'list_loker.html', context)

def list_artikel(request):
    artikel = Artikel.objects.all()
    context = {'artikel' : artikel}

    return render(request,'list_artikel.html', context)

def detail_berita(request, id):
    detail_berita = Event.objects.get(id=id)
    context = {'detail_berita' : detail_berita }

    return render(request,'detail_berita.html', context)

def detail_resensi(request, id):
    detail_resensi = Buku.objects.get(id=id)
    context = {'detail_resensi' : detail_resensi}

    return render(request,'detail_resensi.html', context)

def detail_artikel(request, id):
    detail_artikel = Artikel.objects.get(id=id)
    context = {'detail_artikel' : detail_artikel}

    return render(request,'detail_artikel.html', context)

def detail_loker(request, id):
    detail_loker = Loker.objects.get(id=id)
    context = {'detail_loker' : detail_loker}

    return render(request,'detail_loker.html', context)

def alumni(request):
    alumni = Profile.objects.all().order_by('user__first_name')
    items_per_page = 5
    paginator = Paginator(alumni, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, }

    return render(request,'daftaralumni.html', context)


def testpagination(request):
    queryset = Profile.objects.all()
    items_per_page = 5
    paginator = Paginator(queryset, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
    'page': page,
}

    return render(request, 'paginated.html', context)

def detail_alumni(request, id):
    detail_alumni = Profile.objects.get(id=id)
    context = {'detail_alumni' : detail_alumni}

    return render(request,'detail_alumni.html', context)

def detail_angkatan(request, angkatan):
    detail_angkatan = Profile.objects.filter(angkatan=angkatan)
    context = {'detail_angkatan' : detail_angkatan}

    return render(request,'detail_angkatan.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

def pekerjaan_chart(request):
    labels = []
    data = []
    queryset = Survei.objects.values('tempat_kerja').annotate(langcount=Count('tempat_kerja'))
    for xlang in queryset:
      labels.append(xlang['tempat_kerja'])
      data.append(xlang['langcount'])
    return render(request, 'chart_pekerjaan.html',{'labels' : labels,'data' : data,})

def institusi_chart(request):
    labels = []
    data = []
    queryset = Survei.objects.values('jenis_instansi').annotate(langcount=Count('jenis_instansi'))
    for xlang in queryset:
      labels.append(xlang['jenis_instansi'])
      data.append(xlang['langcount'])
    return render(request, 'chart_instansi.html',{'labels' : labels,'data' : data,})

def jabatan_chart(request):
    labels = []
    data = []
    queryset = Survei.objects.values('jabatan').annotate(langcount=Count('jabatan'))
    for xlang in queryset:
      labels.append(xlang['jabatan'])
      data.append(xlang['langcount'])
    return render(request, 'chart_jabatan.html',{'labels' : labels,'data' : data,})



