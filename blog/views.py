from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.


def home(request):

    services = ["Coding.", "Eating.", "Sleeping."]
    date_today = "06-sept"
    context = {
        'heading': 'APE ON THE MOON.',
        'services': services,
        'posts' :["Big Blue World", "Out of Space","A-O A-Okay"],
        'date': date_today,
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
    

def postDetail (request):

    context = {
        'heading' : 'Related Posts',
        'posts' :["I am number 4","Wildlife","Adventure"]

    }

    return render(request, 'blog/post-detail.html', context)

