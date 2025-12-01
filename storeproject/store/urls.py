from django.urls import path
from .views import home, creators, creator, login_view, logout_view, register_view, info_view, videos

urlpatterns = [
    path('home/', home, name='store-home'),
    path('creators/', creators, name='store-creators'),
    path('creator/<int:pk>/', creator, name='store-creator'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('info/', info_view, name='store-info'),
    path('videos/', videos, name = 'store-videos'),
]

app_name = 'store'
