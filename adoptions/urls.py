from django.urls import path
from . import views

urlpatterns = [
    path('', views.dog_list, name='dog_list'),
    path('support/', views.support, name='support'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:dog_id>/', views.dog_detail, name='dog_detail'),
    path('<int:dog_id>/adopt/', views.adopt_dog, name='adopt_dog'),
]
