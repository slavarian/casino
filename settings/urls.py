
''' MAIN URLS'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("random", include("randoms.urls")),
    path("auth", include("auths.urls")),
    path("", include("main.urls"))

]
