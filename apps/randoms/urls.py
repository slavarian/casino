
''' RANDOMS URLS'''


from django.contrib import admin
from django.urls import path

from randoms.views import RandomView, slot_mashine

urlpatterns = [
    path('slot_mashine/', slot_mashine),
    path('wheel/', RandomView.as_view(), name='random'),
    # path('', RandomView.as_view(), name='random'),
]
