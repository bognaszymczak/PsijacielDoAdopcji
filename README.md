Psijaciel Do Adopcji (Dog Adoption Platform)

A full-stack web application designed to facilitate the dog adoption process. The platform allows users to browse available dogs, filter results by breed or age, and submit adoption applications directly through a modern, responsive interface.

Key Features
**Smart Search & Filtering:** Users can search for dogs by name, breed, and age range.
**Detailed Profiles:** Individual pages for every dog featuring photos and descriptions.
**Adoption Flow:** Integrated form for submitting adoption applications.
**User System:** Secure registration and login authentication system.
**Modern UI:** A warm, user-friendly interface built with Bootstrap 5 and custom CSS.
**Admin Panel:** Easy management of dog profiles via the Django Admin interface.

Tech Stack
**Backend:** Python 3, Django Framework
**Frontend:** HTML5, CSS3, Bootstrap 5
**Database:** SQLite (Development)

*************************

EN

Setup Instructions

Clone the repository Open a terminal and run: (Bash) git clone https://github.com/bognaszymczak/PsijacielDoAdopcji.git cd PsijacielDoAdopcji

Create and activate a virtual environment: (Windows Bash) python -m venv venv source venv/Scripts/activate

(Windows PowerShell) python -m venv venv venv\Scripts\activate

(MacOS/Linux) python3 -m venv venv source venv/bin/activate

Install required dependencies: pip install -r requirements.txt

Database configuration: python manage.py migrate

Create an administrator account: (follow the prompts) python manage.py createsuperuser

Import sample dog data from the API: python manage.py import_dogs

Run the server: python manage.py runserver

The site is available at: http://127.0.0.1:8000/


**************************


PL

Instrukcja uruchomienia

1. Pobranie kodu
Otwórz terminal i sklonuj repozytorium:
(Bash)
git clone [https://github.com/bognaszymczak/PsijacielDoAdopcji.git](https://github.com/bognaszymczak/PsijacielDoAdopcji.git)
cd PsijacielDoAdopcji

2. Otwórz i aktywuj środowisko:
(Windows Bash)
python -m venv venv
source venv/Scripts/activate

(Windows PoweShell)
python -m venv venv
venv\Scripts\activate

(MacOS/Linux)
python3 -m venv venv
source venv/bin/activate

4. Zainstaluj wymagane biblioteki:
pip install -r requirements.txt

5. Konfiguracja bazy danych:
python manage.py migrate

6. Stwórz konto administratora:
(login/hasło)
python manage.py createsuperuser

7. Pobranie przykładowych psów z API
python manage.py import_dogs

8. Uruchom server:
python manage.py runserver

9. Strona jest dostępna pod adresem:
http://127.0.0.1:8000/


*******************************


Design & UI Concept
The application design was created in Figma before implementation, focusing on a warm, friendly aesthetic suitable for animal adoption.

Figma Design Concept: (https://www.figma.com/design/WFs2apntRrHflClZ3ZOjPT/Psijaciel-Do-Adopcji?node-id=0-1&p=f&t=KcT8Ph6fFYvX9oDM-0)

*Original design mockups showing the user journey from browsing to adoption success.*
