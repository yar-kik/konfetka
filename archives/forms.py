from django import forms

from archives.models import Film, Anime, Game


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        labels = {
            'tags': 'Теги',
            'genres': 'Жанри',
        }
        widgets = {
            'release_date': forms.NumberInput(attrs={'min_value': 1900, 'max_value': 2025})
        }


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
