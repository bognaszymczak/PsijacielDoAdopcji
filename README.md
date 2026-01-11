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
