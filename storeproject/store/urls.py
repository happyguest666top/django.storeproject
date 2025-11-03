from django.urls import path
from store.views import home, creators, creator

urlpatterns = [
    path('home/', home, name='store-home'),
    path('creators/', creators, name='store-creators'),
    path('creator/<int:pk>/', creator, name='store-creator'),
]

app_name = 'store'
