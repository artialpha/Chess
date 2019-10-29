from django.db import models
from django.db.models import Avg
# Create your models here.
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Player(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)
    opening = models.ForeignKey(
        'chess.ChessOpening',
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    image = models.URLField(blank=True, null=True)

    @property
    def average_rating(self):
        return vars(type(self).objects.annotate(Avg('playerrate__rate')).filter(name=self.name)[0])['playerrate__rate__avg']

    def __str__(self):
        return self.name+" "+str(self.id)


class PlayerRate(models.Model):
        rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
        player = models.ForeignKey(
            Player,
            on_delete=models.CASCADE,
            blank=True, null=True
        )

        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            blank=True, null=True
        )

        def __str__(self):
            string = str(self.player.name)+" "+str(self.rate)+" "+str(self.user.username)
            return string

