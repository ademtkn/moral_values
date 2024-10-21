from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa yönlendirmesi
    path('categories/', views.category_list, name='category_list'),  # Kategori sayfa yönlendirmesi
    path('categories/<str:category_name>/', views.subcategory_list, name='subcategory_list'),  # Alt kategori sayfa yönlendirmesi
    path('kindergarten/', views.kindergarten_subject_list, name='kindergarten_subject_list'),
    path('subject/<int:subcategory_id>/', views.subject_list, name='subject_list'),
    path('subject/<int:subject_id>/stories/', views.story_list, name='story_list'),
    path('subject/<int:subject_id>/videos/', views.video_list, name='video_list'),
    path('subject/<int:subject_id>/games/', views.game_list, name='game_list'),
    path('subject/<int:subject_id>/songs/', views.song_list, name='song_list'),
    path('subject/<int:subject_id>/resources/', views.resource_list, name='resource_list'),
    path('contact_us/', views.contact_us, name='contact_us'), # Contact Us URL'si
    path('login/', views.login_view, name='login'),  # Login URL'si
    path('register/', views.register_view, name='register'),  # Register URL'si
    path('about-us/', views.about_us, name='about_us'), # About Us URL'si
    path('donate/', views.donate, name='donate'),  # Donate view için URL tanımlaması
    path('process-donation/', views.process_donation, name='process_donation'),
]
