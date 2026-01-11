from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Dog, AdoptionApplication
from .forms import AdoptionForm

def dog_list(request):
    dogs = Dog.objects.filter(is_available=True)
    return render(request, 'dog_list.html', {'dogs': dogs})

def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, 'dog_detail.html', {'dog': dog})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def adopt_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)

    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.dog = dog
            application.user = request.user
            application.save()
            return render(request, 'adoption_success.html', {'dog': dog})
    else:
        form = AdoptionForm()

    return render(request, 'adopt_dog.html', {'form': form, 'dog': dog})