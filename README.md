PL
Instrukcja Uruchomienia (Setup)

Aby uruchomić projekt lokalnie, wykonaj poniższe kroki:

1.  **Klonowanie repozytorium:**
    ```bash
    git clone [https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/PsijacielDoAdopcji.git](https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/PsijacielDoAdopcji.git)
    cd PsijacielDoAdopcji
    ```

2.  **Utworzenie wirtualnego środowiska (zalecane):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalacja zależności:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Przygotowanie bazy danych:**
    ```bash
    python manage.py migrate
    ```

5.  **Utworzenie konta administratora (opcjonalnie):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **(Opcjonalnie) Zaimportowanie przykładowych psów z API:**
    ```bash
    python manage.py import_dogs
    ```

7.  **Uruchomienie serwera:**
    ```bash
    python manage.py runserver
    ```
    Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000/`

    EN
   Setup Instructions

To run the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/PsijacielDoAdopcji.git](https://github.com/YOUR_USERNAME/PsijacielDoAdopcji.git)
    cd PsijacielDoAdopcji
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database setup:**
    ```bash
    python manage.py migrate
    ```

5.  **Create an administrator account (optional):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **(Optional) Import sample dogs from external API:**
    ```bash
    python manage.py import_dogs
    ```

7.  **Run the server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at: `http://127.0.0.1:8000/`
