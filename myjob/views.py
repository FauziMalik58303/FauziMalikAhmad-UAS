from django.shortcuts import render, get_object_or_404, redirect
from artikel.models import Kategori, ArtikelBlog, Komentar
from artikel.forms import KomentarForm


# Beranda/Home
def home(request):
    template_name = 'landingpage/home.html'
    kategori_list = Kategori.objects.all()
    artikel_list = ArtikelBlog.objects.all()

    context = {
        "kategori": kategori_list,
        "artikel": artikel_list,
        "title": "Rental Mobil - Home"
    }
    return render(request, template_name, context)

# Detail Artikel + Komentar
def artikel_detail(request, id):
    artikel = get_object_or_404(ArtikelBlog, id=id)
    kategori_list = Kategori.objects.all()  # Ambil semua kategori
    komentar_list = Komentar.objects.filter(artikel=artikel)  # Ambil semua komentar terkait artikel

    if request.method == 'POST':
        form = KomentarForm(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.user = request.user
            komentar.artikel = artikel
            komentar.save()
            return redirect('artikel_detail', id=artikel.id)
    else:
        form = KomentarForm()

    artikel_lainya = ArtikelBlog.objects.all().exclude(id=id)

    context = {
        'item': artikel,  
        'kategori_list': kategori_list,  # <-- kirim ke template
        'komentar_list': komentar_list,
        'artikel_lainya': artikel_lainya,
        'form': form,
    }
    return render(request, 'landingpage/detail.html', context)

# Halaman Tentang
def about(request):
    template_name = 'about.html'
    context = {
        'title': 'About Me'
    }
    return render(request, template_name, context)

# Berita Bola Statis
def berita_bola(request):
    template_name = 'berita_bola.html'
    berita = [
        {"judul": "Timnas Indonesia Lolos ke Piala Dunia", "tanggal": "21 Maret 2025"},
        {"judul": "Messi Cetak Hattrick Spektakuler!", "tanggal": "20 Maret 2025"},
        {"judul": "Manchester United Juara Liga Champions", "tanggal": "19 Maret 2025"},
    ]
    context = {
        'title': 'Berita Bola Terkini',
        'berita': berita
    }
    return render(request, template_name, context)



def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth_login')
    
    template_name = "dashboard/index.html"
    context = {
        "title":"Selamat datang"
    }
    return render(request, template_name, context)

def artikel_list(request):
    template_name = "dashboard/artikel_list.html"
    context = {
        "title":"Selamat datang"
    }
    return render(request, template_name, context)

