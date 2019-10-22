from django import forms
from .models import PlayerRate
from .models import Player

# the right side = description
FRUIT_CHOICES= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ]


class PlayerRateForm(forms.ModelForm):
    rate = forms.CharField(label='Rate for a player', widget=forms.RadioSelect(choices=FRUIT_CHOICES))

    class Meta:
        model = PlayerRate
        fields = ('rate','player',)


"""

class PlayerRateForm(forms.Form):
    favorite_fruit = forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    player = forms.ModelChoiceField(queryset=Player.objects.all(), empty_label="(Nothing)")
"""

