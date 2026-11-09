from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

# Django's built-in form for creating user accounts.
from django.contrib.auth.forms import UserCreationForm

# Log players in automatically after creating an account.
from django.contrib.auth import login


from .models import Tournament, Registration


# Display all tournaments, ordered by their starting date.
def tournament_list(request):

    # Retrieve tournaments from the SQLite database.
    tournaments = Tournament.objects.order_by('start_time')

    # Make the tournament data available to the HTML template.
    context = {
        'tournaments': tournaments,
    }

    # Render the player-facing tournament listing page.
    return render(
        request,
        'tournaments/tournament_list.html',
        context
    )


# Allow authenticated players to preregister for a tournament.
@login_required
def register_for_tournament(request, tournament_id):

    # Only accept form submissions using the POST method.
    if request.method != 'POST':
        return redirect('tournament_list')

    # Find the requested tournament or return a 404 error.
    tournament = get_object_or_404(Tournament, id=tournament_id)

    # Prevent registration when the tournament is closed.
    if not tournament.registration_open:
        messages.error(request, 'Registration is closed for this tournament.')
        return redirect('tournament_list')

    # Create a registration only if this player has not registered already.
    registration, created = Registration.objects.get_or_create(
        tournament=tournament,
        player=request.user
    )

    # Display feedback depending on whether registration was created.
    if created:
        messages.success(
            request,
            'Preregistration successful! Your tournament spot is not guaranteed until check-in and payment are confirmed.'
        )
    else:
        messages.info(
            request,
            'You are already preregistered for this tournament.'
        )

    # Return the player to the tournament listing.
    return redirect('tournament_list')

# Allow new players to create a MEL Tournament Manager account.
def signup(request):

    # Process the submitted registration form.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # Validate the username and both password fields.
        if form.is_valid():

            # Save the new user account to the database.
            user = form.save()

            # Automatically log in the newly registered player.
            login(request, user)

            # Confirm that account creation was successful.
            messages.success(
                request,
                'Your account has been created successfully!'
            )

            # Send the player to the tournament listing.
            return redirect('tournament_list')

    else:
        # Display an empty registration form for new visitors.
        form = UserCreationForm()

    # Display the signup form and any validation errors.
    return render(
        request,
        'registration/signup.html',
        {'form': form}
    )
