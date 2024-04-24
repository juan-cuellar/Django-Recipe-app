

from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Recipe



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'recipe_description', 'ingredients']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a name'}),
            'recipe_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a recipe_description'}), 
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write a recipe_description'}), 
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
        }


# class UserRegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
        # widgets = {
        #     'username' : forms.TextInput(attrs={'class':'form_control'}),
        #     'password1' : forms.TextInput(attrs={'class':'form_control'}),
        #     'password2' : forms.TextInput(attrs={'class':'form_control'}),
        # }

# class CleanForm(AuthenticationForm):

#     def clean_username(self):
#         return self.cleaned_data['username'].lower()
