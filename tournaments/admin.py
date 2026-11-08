
from django.contrib import admin
from .models import Tournament


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
