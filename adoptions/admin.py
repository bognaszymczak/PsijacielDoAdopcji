from django.contrib import admin
from .models import Breed, Dog, AdoptionApplication

admin.site.register(Breed)

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'is_available')
    list_filter = ('breed', 'is_available')
    search_fields = ('name',)

@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'dog', 'status', 'date_applied')
    list_filter = ('status',)
    actions = ['accept_application', 'reject_application']

    def accept_application(self, request, queryset):
        queryset.update(status='accepted')
    accept_application.short_description = "Zatwierdź wybrane wnioski"

    def reject_application(self, request, queryset):
        queryset.update(status='rejected')
    reject_application.short_description = "Odrzuć wybrane wnioski"