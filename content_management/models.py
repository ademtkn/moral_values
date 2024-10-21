from django.db import models
from django_ckeditor_5.fields import CKEditor5Field  # CKEditor 5 alanı import ediyoruz

# Ana Kategori Modeli
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Alt Kategori (Grade) Modeli
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

# Konu (Subject) Modeli
class Subject(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

# Story Modeli
class Story(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# Video Modeli (ForeignKey ile Subject'e bağlandı)
class Video(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()  # Video bağlantısı

    def __str__(self):
        return self.title

# Game Modeli (ForeignKey ile Subject'e bağlandı)
class Game(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Song (MP3) Modeli (ForeignKey ile Subject'e bağlandı)
class Song(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='songs/')  # MP3 dosyası

    def __str__(self):
        return self.title

# Resources Modeli (ForeignKey ile Subject'e bağlandı)
class Resource(models.Model):
    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF'),
        ('jpg', 'JPG'),
        ('png', 'PNG'),
        ('ppt', 'PowerPoint'),
        ('doc', 'Word Document'),
        ('xls', 'Excel'),
        ('zip', 'ZIP')
    ]
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='resources/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES)

    def __str__(self):
        return self.title
