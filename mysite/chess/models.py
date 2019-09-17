from django.db import models


class ChessOpening(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    eco = models.CharField(max_length=200)


class Variant(models.Model):
    chess_opening = models.ForeignKey(ChessOpening, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    moves = models.TextField()
    number = models.DecimalField(decimal_places=0, max_digits=2)
    description = models.TextField(blank=True)