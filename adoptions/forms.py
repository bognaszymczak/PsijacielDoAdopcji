from django import forms
from .models import AdoptionApplication

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['phone_number', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Napisz, dlaczego chcesz adoptować tego psa...'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Np. 500 123 456'}),
        }