
from django.db import models


# Stores information about each MEL tournament.
class Tournament(models.Model):

    # The name displayed to players.
    name = models.CharField(max_length=100)

    # Date and time when the tournament begins.
    start_time = models.DateTimeField()

    # Physical location hosting the tournament.
    location = models.CharField(max_length=200)

    # Maximum number of players allowed to participate.
    max_players = models.PositiveIntegerField(default=16)

    # Indicates whether registration is available.
    registration_open = models.BooleanField(default=True)

    # Provides a readable tournament name in Django Admin.
    def __str__(self):
        return self.name

