from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Dog, Breed
from .forms import AdoptionForm


 
# LISTA PSÓW + FILTROWANIE

def dog_list(request):
    dogs = Dog.objects.filter(is_available=True)

 
    breed_id = request.GET.get("breed")
    min_age = request.GET.get("min_age")
    max_age = request.GET.get("max_age")
    q = request.GET.get("q")

    if breed_id:
        dogs = dogs.filter(breed_id=breed_id)

    if min_age:
        try:
            dogs = dogs.filter(age__gte=int(min_age))
        except ValueError:
            pass

    if max_age:
        try:
            dogs = dogs.filter(age__lte=int(max_age))
        except ValueError:
            pass

    if q:
        dogs = dogs.filter(name__icontains=q)

    breeds = Breed.objects.all().order_by("name")

    context = {
        "dogs": dogs,
        "breeds": breeds,
        "selected_breed": breed_id or "",
        "min_age": min_age or "",
        "max_age": max_age or "",
        "q": q or "",
    }

    return render(request, "dog_list.html", context)


# SZCZEGÓŁY PSA
def dog_detail(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    return render(request, "dog_detail.html", {"dog": dog})


# STRONA WSPARCIA
def support(request):
    return render(request, "support.html")


# REJESTRACJA

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



# ADOPCJA PSA

@login_required
def adopt_dog(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)

    if request.method == "POST":
        form = AdoptionForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.dog = dog
            application.user = request.user
            application.save()

            return render(request, "adoption_success.html", {"dog": dog})
    else:
        form = AdoptionForm()

    return render(
        request,
        "adopt_dog.html",
        {
            "form": form,
            "dog": dog,
        },
    )
