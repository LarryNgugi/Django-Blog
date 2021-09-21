from typing import ClassVar
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Feedback, Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from blog.forms import CommentForm

# Create your views here.


def home(request):

    context = {
        'heading': 'APE ON THE MOON.',
        'services': Category.objects.all()[:3],
        'posts': Post.objects.all()[:6]
    }

    return render(request, "home.html", context)

def getPostDetails(request,id):

    our_post : Post.objects.get(pk = id)

    context = {
        'post' : our_post,
        'categories': Category.objects.all(),
        'posts' : Post.objects.filter(category = our_post.category).exclude(pk = our_post.id),
        'commentForm' : CommentForm(),

    }
    return render(request, "blog/post-detail.html", context)


def contact(request):

    context = {
        'heading': 'Contact Me',
        'phone': "(+254) 714 389 500",
        'address': "Nairobi, Kenya",
        'email': "larry.josephgithaka@gmail.com",
    }

    return render(request, "contact.html", context)


def blog(request):
    context = {

        'posts': ["Big Blue World", "Out of Space", "A-O A-Okay", "I am number 4", "Wildlife", "Adventure"]

    }

    return render(request, "blog/blog.html", context)


def postDetail(request):

    context = {
        'heading': 'Related Posts',
        'posts': ["I am number 4", "Wildlife", "Adventure"]

    }

    return render(request, 'blog/post-detail.html', context)


def dashboard(request):
    context = {

    }

    return render(request, 'blog/admin/dashboard.html', context)


def saveFeedback(request):

    name = request.POST.get("name")
    email = request.POST.get("email")
    phone_number = request.POST.get("number")
    message = request.POST.get("message")

    Feedback.objects.create(name=name, email=email,phone_number=phone_number, message=message)

    context = {}

    return HttpResponseRedirect('/contact')


def showFeedback(request):

    context = {}
    context['feedback_list'] = Feedback.objects.all()

    return render(request, 'blog/admin/feedback.html', context)


def showCategory(request):

    context = {
        'category_list': Category.objects.all()
    }
    return render(request, 'blog/admin/categories.html', context)


def categoryForm(request):
    context = {}

    return render(request, 'blog/admin/category-form.html', context)


def storeCategory(request):
    Category_name = request.POST.get("name")
    Category.objects.create(name=Category_name)

    return HttpResponseRedirect('/staff/categories')


def deleteCategory(request, id):

    our_category = Category.objects.get(pk=id)
    our_category.delete()

    return HttpResponseRedirect('/staff/categories')


def deleteFeedback(request, id):

    our_feedback = Feedback.objects.get(pk=id)
    our_feedback.delete()

    return HttpResponseRedirect('/staff/feedback')





class PostList(ListView):
    model = Post
    template_name = "blog/admin/posts.html"


class PostCreate(CreateView):
    model = Post
    template_name = "blog/admin/post-form.html"
    fields = "__all__"
    success_url = '/staff/posts'


class PostDetails(DetailView):
    model = Post
    template_name = "blog/admin/post_detail.html"
    context_object_name = "post"

class PostUpdate(UpdateView):
    model = Post
    fields = ['tittle','message','slug','Category','user','keywords','image_url']
    success_url = '/staff/posts'
    template_name = "blog/admin/post-form.html"
