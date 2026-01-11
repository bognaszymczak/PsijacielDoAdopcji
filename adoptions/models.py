from django.db import models
from django.contrib.auth.models import User

# Model 1: Rasa psa
class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa rasy")

    def __str__(self):
        return self.name

# Model 2: Pies
class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name="Imię psa")
    age = models.PositiveIntegerField(verbose_name="Wiek")
    description = models.TextField(verbose_name="Opis")
    image = models.ImageField(upload_to='dogs/', verbose_name="Zdjęcie", blank=True, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name="Rasa")
    is_available = models.BooleanField(default=True, verbose_name="Dostępny do adopcji")

    def __str__(self):
        return self.name

# Model 3: Wniosek adopcyjny
class AdoptionApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekujący'),
        ('accepted', 'Zaakceptowany'),
        ('rejected', 'Odrzucony'),
    ]

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, verbose_name="Pies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Użytkownik")
    message = models.TextField(verbose_name="Wiadomość do schroniska")
    phone_number = models.CharField(max_length=15, verbose_name="Numer telefonu")
    date_applied = models.DateTimeField(auto_now_add=True, verbose_name="Data złożenia")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Status")

    def __str__(self):
        return f"{self.user.username} - {self.dog.name}"