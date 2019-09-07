from django.db import models


class ChessOpenings(models.Model):
    name_of_opening = models.CharField(max_length=200)