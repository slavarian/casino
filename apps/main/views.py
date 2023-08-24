"""MAIN APP"""
from typing import Any

from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http.request import HttpRequest

import random

from .models import (
    Reclama
)

def main_page(request:HttpRequest ):
    total_models = Reclama.objects.count()
    random_model_id = random.randint(1, total_models)
    random_model = Reclama.objects.get(id=random_model_id)
    return render(
        template_name='main.html',
        request=request,
        context={
            'random_model':random_model
        }
    )
