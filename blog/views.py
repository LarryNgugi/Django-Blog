from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    context = {
        'heading': 'My First Blog!',
        'services': ["Coding.", "Eating.", "Sleeping."],
        'posts' :["Big Blue World", "Out of Space","A-O A-Okay"]
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

def blog (request):
    context = {
         'posts' :["Big Blue World", "Out of Space","A-O A-Okay","I am number 4","Wildlife","Adventure"]
    }

    return render(request, "blog/blog.html", context)


