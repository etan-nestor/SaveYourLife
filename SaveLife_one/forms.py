from django import forms
from .models import Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]

        labels = {
            "name": "Votre nom",
            "email": "Email",
            "body": "Votre commentaire ici",
        }

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control rounded shadow-sm', 'placeholder': 'Your name ', 'style': 'width: 40%;'}),
            "email": forms.EmailInput(attrs={'class': 'form-control rounded shadow-sm', 'placeholder': 'Your Email', 'style': 'width: 40%;'}),
            "body": forms.Textarea(attrs={'class': 'form-control rounded shadow-sm', 'placeholder': 'Your comment here !', 'rows': 5, 'style': 'width: 100%;'}),
        }
