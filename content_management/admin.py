from django.contrib import admin
from .models import Category, SubCategory, Subject, Story, Video, Game, Song, Resource
from ckeditor.widgets import CKEditorWidget
from django import forms

# CKEditor'ı kullanmak için ModelForm oluşturuyoruz
class StoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Story
        fields = '__all__'

class GameAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Game
        fields = '__all__'

# Story ve Game modellerine CKEditor'u entegre ediyoruz
class StoryAdmin(admin.ModelAdmin):
    form = StoryAdminForm
    list_display = ['title', 'subject']

class GameAdmin(admin.ModelAdmin):
    form = GameAdminForm
    list_display = ['title', 'subject']

# Inline modelleri tanımlıyoruz
class StoryInline(admin.TabularInline):
    model = Story
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class GameInline(admin.TabularInline):
    model = Game
    extra = 1

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1

# Subject modelini düzenliyoruz
class SubjectAdmin(admin.ModelAdmin):
    inlines = [StoryInline, VideoInline, GameInline, SongInline, ResourceInline]
    list_display = ['name', 'subcategory']
    list_display_links = ['name']
    list_filter = ['subcategory', 'subcategory__category']
    search_fields = ['name']

# SubCategory ve Category modelini düzenliyoruz
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']

# Modelleri kaydediyoruz
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Story, StoryAdmin)  # CKEditor ile Story modelini kaydediyoruz
admin.site.register(Video)
admin.site.register(Game, GameAdmin)  # CKEditor ile Game modelini kaydediyoruz
admin.site.register(Song)
admin.site.register(Resource)
