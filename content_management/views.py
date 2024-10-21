from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Subject, Story, Video, Game, Song, Resource

# Ana sayfa görünümü
def home(request):
    return render(request, 'home.html')

def home(request):
    # En son eklenen içerikler
    latest_stories = Story.objects.all().order_by('-id')[:5]
    latest_videos = Video.objects.all().order_by('-id')[:5]
    latest_games = Game.objects.all().order_by('-id')[:5]
    latest_songs = Song.objects.all().order_by('-id')[:5]
    latest_resources = Resource.objects.all().order_by('-id')[:5]
    

    return render(request, 'home.html', {
        'latest_stories': latest_stories,
        'latest_videos': latest_videos,
        'latest_games': latest_games,
        'latest_songs': latest_songs,
        'latest_resources': latest_resources,
    })

def about_us(request):
    return render(request, 'about_us.html')

# Login View Fonksiyonu
def login_view(request):
    return render(request, 'login.html')  # login.html dosyasını döndürür

def register_view(request):
    return render(request, 'register.html')

# Kategorileri listeleyen görünüm
def category_list(request):
    return render(request, 'category_list.html')

# İçerikleri listeleyen görünüm
def content_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    stories = Story.objects.filter(subject=subject)
    videos = Video.objects.filter(subject=subject)
    games = Game.objects.filter(subject=subject)
    songs = Song.objects.filter(subject=subject)
    resources = Resource.objects.filter(subject=subject)

def subcategory_list(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    subcategories = SubCategory.objects.filter(category=category)
    return render(request, 'subcategory_list.html', {'category': category, 'subcategories': subcategories})

    # Tüm içerikleri bir arada gönderiyoruz
    return render (request, 'content_list.html', {
        'subject': subject,
        'stories': stories,
        'videos': videos,
        'games': games,
        'songs': songs,
        'resources': resources,
    })


# Kindergarten için konuları listeleyen görünüm
def kindergarten_subject_list(request):
    subjects = Subject.objects.filter(subcategory__isnull=True)  # Subcategory boş olan (Kindergarten'a bağlı) konuları getir
    return render(request, 'subject_list.html', {'subjects': subjects})

# Story listeleyen görünüm
def story_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    stories = Story.objects.filter(subject=subject)
    return render(request, 'story_list.html', {'subject': subject, 'stories': stories})

# Video listeleyen görünüm
def video_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    videos = Video.objects.filter(subject=subject)
    return render(request, 'video_list.html', {'subject': subject, 'videos': videos})

# Game listeleyen görünüm
def game_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    games = Game.objects.filter(subject=subject)
    return render(request, 'game_list.html', {'subject': subject, 'games': games})

# Song (MP3) listeleyen görünüm
def song_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    songs = Song.objects.filter(subject=subject)
    return render(request, 'song_list.html', {'subject': subject, 'songs': songs})

# Resource (Dökümanlar) listeleyen görünüm
def resource_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    resources = Resource.objects.filter(subject=subject)
    return render(request, 'resource_list.html', {'subject': subject, 'resources': resources})


def subject_list(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    subjects = Subject.objects.filter(subcategory=subcategory)
    return render(request, 'subject_list.html', {'subcategory': subcategory, 'subjects': subjects})

# About Us sayfası görünümü
def about_us(request):
    return render(request, 'about_us.html')

# İletişim sayfası görünümü
def contact_us(request):
    return render(request, 'contact_us.html')

# Donate sayfasi
def donate(request):
    return render(request, 'donate.html') 

def process_donation(request):
    if request.method == 'POST':
        # Burada formdan gelen bilgileri işleyebilirsin
        # Örneğin, bağış miktarını ve bilgileri kaydedebilirsin
        return HttpResponse("Bağış için teşekkür ederiz!")
    else:
        return redirect('donate')


