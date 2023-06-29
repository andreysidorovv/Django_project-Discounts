

from django.shortcuts import render
from .models import Discount, SpecialOffer


def discounts(request):
    obj = Discount.objects.all()
    context = {
        "obj": obj,
    }
    return render(request, 'discount.html', context)

def special_offers(request):
    obj = SpecialOffer.objects.all()
    context = {
        "obj": obj,
    }
    return render(request, 'discount.html', context)


