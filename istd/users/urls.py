from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('activation/<activation_url>', after_register, name='after_register')
]

urlpatterns += [
    path('profile/', UserCabinetTemplate.as_view(), name='cabinet'),
    path('profile/account/', UserCabinetChangeTemplate.as_view(), name='change_info')
]
