from django import forms
from .models import SuperHero

class SuperHeroForm(forms.ModelForm):
    """
    Form for filling in superhero info
    """
    class Meta:
        model = SuperHero
        fields = ["name", "secret_identity", "first_appearance"]
