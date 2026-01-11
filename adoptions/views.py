from django.shortcuts import render, get_object_or_404
from .models import Dog

def dog_list(request):
    dogs = Dog.objects.filter(is_available=True)
    return render(request, 'dog_list.html', {'dogs': dogs})

def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})