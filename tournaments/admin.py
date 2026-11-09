from django.contrib import admin
from .models import Tournament, Registration


# Configure how tournaments appear in Django Admin.
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):

    # Display these fields in the tournament list.
    list_display = (
        'name',
        'start_time',
        'location',
        'max_players',
        'registration_open',
    )

    # Allow administrators to filter tournaments.
    list_filter = ('registration_open', 'start_time')

    # Allow administrators to search by tournament name or location.
    search_fields = ('name', 'location')

# Allow organizers to manage player registrations through Django Admin.
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    # Show important registration details in the admin list.
    list_display = (
        'player',
        'tournament',
        'registered_at',
        'checked_in',
        'payment_confirmed',
    )

    # Allow organizers to filter registrations by status.
    list_filter = (
        'tournament',
        'checked_in',
        'payment_confirmed',
    )

    # Allow searching for registrations by player username.
    search_fields = ('player__username',)

    # Registration timestamps are generated automatically.
    readonly_fields = ('registered_at',)
