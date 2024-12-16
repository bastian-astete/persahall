from django import forms
from .models import CustomUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'nickname', 'birth_date', 'profile_picture', 'direccion']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }