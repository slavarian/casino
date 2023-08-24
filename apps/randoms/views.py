'''RANDOM VIEWS'''
import random


from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse




class RandomView(View):
    """Класс, который служит для рандомных штук"""

    def get(self, request):
        random_number = random.randint(0, 100)
        context = {
            'random_number': random_number
        }
        return render(
            template_name='random/wheel.html',
            request=request,
            context = context
        )

def slot_mashine(request):
    return render(
        template_name='random/slot_mashine.html',
        request=request
    )