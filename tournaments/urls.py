from django.urls import path
from . import views


# Define the URLs handled by the tournaments application.
urlpatterns = [

    # Display the list of available tournaments.
    path(
        '',
        views.tournament_list,
        name='tournament_list'
    ),

    # Process player preregistration for a specific tournament.
    path(
        '<int:tournament_id>/register/',
        views.register_for_tournament,
        name='register_for_tournament'
    ),

    # Allow new players to create an account.
    path(
        'signup/',
        views.signup,
        name='signup'
    ),
]
