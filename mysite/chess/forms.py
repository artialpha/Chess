from django import forms

from .models import ChessOpening


class ChessOpeningForm(forms.ModelForm):
    class Meta:
        model = ChessOpening
        fields = [
            'name',
            'description',
            'eco',
        ]

