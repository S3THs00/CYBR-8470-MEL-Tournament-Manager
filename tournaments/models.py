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

# Stores a player's preregistration for a tournament.
class Registration(models.Model):

    # Connect each registration to an existing tournament.
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    # Connect the registration to a Django user account.
    player = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='tournament_registrations'
    )

    # Record when the player preregistered.
    registered_at = models.DateTimeField(auto_now_add=True)

    # Organizers manually confirm check-in and payment.
    checked_in = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)

    # Prevent the same account from registering twice.
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tournament', 'player'],
                name='unique_tournament_player'
            )
        ]

    # Display readable registration information in Django Admin.
    def __str__(self):
        return f"{self.player.username} - {self.tournament.name}"
