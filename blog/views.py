from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    context = {
        'heading': 'My First Blog!',
        'services': ["Coding.", "Eating.", "Sleeping."],
    }

    return render(request, "home.html", context)


def contact(request):

    context = {
        'heading' : 'Contact Me',
        'phone': "(+254) 714 389 500",
        'address': "Nairobi, Kenya",
        'email': "larry.josephgithaka@gmail.com",
    }

    return render(request, "contact.html", context)
