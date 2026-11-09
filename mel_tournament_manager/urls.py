from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


# Main URL routes for the MEL Tournament Manager.
urlpatterns = [

    # Redirect visitors from the homepage to the login page.
    path(
        '',
        RedirectView.as_view(pattern_name='login', permanent=False),
        name='home'
    ),

    # Django's built-in administration interface.
    path('admin/', admin.site.urls),

    # Player-facing tournament pages.
    path('tournaments/', include('tournaments.urls')),

    # Django's built-in authentication routes.
    # Provides login and logout functionality.
    path('accounts/', include('django.contrib.auth.urls')),

]
