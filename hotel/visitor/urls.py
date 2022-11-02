from django.urls import path

from .views import visitorDetails, visitorOut, addGuest

urlpatterns = [

    path('vd/', visitorDetails),
    path('vo/', visitorOut),
    path('g/', addGuest),
]