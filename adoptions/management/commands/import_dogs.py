import requests
import random
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from adoptions.models import Dog, Breed


class Command(BaseCommand):
    help = 'Pobiera psy z zewnętrznego API i zapisuje w bazie'

    def handle(self, *args, **kwargs):
        self.stdout.write("Rozpoczynam pobieranie psów...")

        names = ['Burek', 'Azor', 'Luna', 'Max', 'Bella', 'Charlie', 'Daisy', 'Rocky', 'Molly', 'Simba']
        descriptions = [
            "Bardzo przyjazny i energiczny pies.",
            "Spokojny kanapowiec, kocha dzieci.",
            "Potrzebuje dużo ruchu i długich spacerów.",
            "Idealny stróż domu, wierny i oddany.",
            "Trochę nieśmiały, ale po poznaniu to wielki pieszczoch."
        ]

        for i in range(10):
            try:
                # 1. Pobranie danych z API
                response = requests.get('https://dog.ceo/api/breeds/image/random')
                data = response.json()
                image_url = data['message']

                # Wyciągnięcie rasy z linku URL
                breed_name = image_url.split('/')[-2].capitalize()

                # 2. Utworzenie lub pobranie Rasy w bazie
                breed_obj, created = Breed.objects.get_or_create(name=breed_name)

                # 3. Pobranie samego obrazka
                image_response = requests.get(image_url)

                if image_response.status_code == 200:
                    # Losowanie danych
                    name = random.choice(names)
                    age = random.randint(1, 12)
                    desc = random.choice(descriptions)

                    # Tworzenie obiektu Psa
                    dog = Dog(
                        name=name,
                        age=age,
                        description=desc,
                        breed=breed_obj,
                        is_available=True
                    )

                    # Zapisanie pliku zdjęcia w Django
                    file_name = f"{name}_{random.randint(1, 1000)}.jpg"
                    dog.image.save(file_name, ContentFile(image_response.content))

                    dog.save()
                    self.stdout.write(self.style.SUCCESS(f'Dodano psa: {name} ({breed_name})'))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Błąd przy imporcie psa: {e}'))

        self.stdout.write(self.style.SUCCESS('Zakończono importowanie!'))