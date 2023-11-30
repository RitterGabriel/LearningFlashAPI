# LearningFlashAPI

LearningFlashAPI serves as the RESTful API supporting the LearningFlash application. This API is built using Django and Django Rest Framework, providing functionalities to manage flashcards and decks and facilitate language learning through spaced repetition.

## Features

- **Flashcard Management:** CRUD operations for managing flashcards and decks.
- **Spaced Repetition Support:** Implement spaced repetition algorithms to optimize learning efficiency.
- **Literature Summary Integration:** Provide access to summaries of English literary works for creating flashcards.

## Tech Stack

- **Backend Framework:** Django with Django Rest Framework
- **Database:** PostgreSQL

## Getting Started

To set up the backend, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/seu-usuario/LearningFlashAPI.git
   ```

2. **Install Dependencies:**
   ```bash
   cd LearningFlashAPI
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The backend provides the following API endpoints:

- **Flashcards:** `/api/decks/<int:id>/flashcards/`
  - GET: Retrieve all flashcards related to a deck.
  - POST: Add a new flashcard to a deck.

- **Decks:** `/api/decks/`
  - GET: Retrieve all decks or create a new deck.
  - POST: Create a new deck.

- **Literature Summaries:** `/api/summaries/`
  - GET: Retrieve all literature summaries.

- **Additional Endpoints:** [List any other endpoints or functionalities here.]



