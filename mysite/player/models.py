from django.db import models

# Create your models here.


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