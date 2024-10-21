from django import forms
from .models import Category, SubCategory, Subject, Resource

# Dinamik olarak SubCategory'leri güncelleyen bir form
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'subject', 'file', 'file_type']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.none(), required=False)
    subject = forms.ModelChoiceField(queryset=Subject.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.subject.subcategory:
            self.fields['subcategory'].queryset = SubCategory.objects.filter(category=self.instance.subject.subcategory.category)
        
        if 'subcategory' in self.data:
            try:
                subcategory_id = int(self.data.get('subcategory'))
                self.fields['subject'].queryset = Subject.objects.filter(subcategory_id=subcategory_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subject'].queryset = Subject.objects.filter(subcategory=self.instance.subject.subcategory)
