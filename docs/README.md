# Project Documentation

This directory contains the project requirements,
user stories, security considerations, interface
mockups, and architecture diagrams for the
Midwest Esports League Tournament Manager.

## User Stories

### User Story 1: Tournament Registration

As a **player**, I want to **register for an upcoming esports tournament**, so I can **express my interest in participating and receive priority during event check-in**.

**Acceptance Criteria:**

- Players can view upcoming tournaments.
- Players can submit their name, gamer tag, and email address.
- Players can select an available tournament.
- The application records the registration date and time.
- Players receive an on-screen confirmation after registering.
- The confirmation clearly states that preregistration does not guarantee a tournament spot.
- Tournament spots are secured only after payment and check-in at the event.

### User Story 2: Tournament Management

As a **tournament organizer**, I want to **create and manage esports tournaments**, so I can **organize events and track player participation efficiently**.

**Acceptance Criteria:**

- Organizers can create tournaments with a name, date, time, location, and maximum number of participants.
- Organizers can view and edit existing tournaments.
- Organizers can view the list of registered players for each tournament.
- The application displays the number of registered players and available tournament spots.
- Only authorized organizers can create, edit, or delete tournaments.


### User Story 3: Match Results and Player Records

As a **tournament organizer**, I want to **record match results and track player wins and losses**, so I can **monitor tournament progress and maintain accurate player records**.

**Acceptance Criteria:**

- Organizers can select two registered players for a match.
- Organizers can record the winner and loser.
- The application automatically updates each player's win and loss totals.
- Organizers can view player records for each tournament.
- Only authorized organizers can enter or modify match results.
- Correcting a match result updates the affected player records.


### User Story 4: Tournament Check-In and Payment Confirmation

As a **tournament organizer**, I want to **check in registered players and confirm their payments**, so I can **accurately manage tournament participation and available spots**.

**Acceptance Criteria:**

- Organizers can view all preregistered players for a tournament.
- Organizers can mark players as checked in.
- Organizers can manually confirm whether payment has been received.
- The first 15 minutes of check-in are reserved for preregistered players.
- During the final 15 minutes, organizers can add walk-in players to remaining available spots.
- Preregistration does not guarantee a tournament spot.
- A tournament spot is secured only after check-in and payment confirmation.
- The application prevents confirmed participants from exceeding the tournament's maximum capacity.
- Only authorized organizers can modify check-in and payment statuses.

## Mis-User Stories

## Interface Mockups

## C4 Architecture Diagrams
