from django.shortcuts import render
from .models import Dog

def dog_list(request):
    dogs = Dog.objects.filter(is_available=True)
    return render(request, 'dog_list.html', {'dogs': dogs})