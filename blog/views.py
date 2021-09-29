from django import forms
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Feedback, Post,Comment,User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from blog.forms import CommentForm,MailForm
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.core.mail import send_mail



# Create your views here.


def home(request):

    num_of_visits = request.session.get("num_of_visits",0)
    request.session["num_of_visits"] = num_of_visits + 1

    context = {
        'heading': 'APE ON THE MOON.',
        'services': Category.objects.all()[:3],
        'posts': Post.objects.all()[:6],
        'num_of_visits' : num_of_visits,
    }

    return render(request, "home.html", context)

def getPostDetails(request,id):

    our_post = Post.objects.get(pk = id)


    our_post.views += 1
    our_post.save()

    our_post.Category.views += 1
    our_post.Category.save()

    

    context = {
        'post' : our_post,
        'categories': Category.objects.all(),
        'posts' : Post.objects.filter(Category = our_post.Category).exclude(pk = our_post.id),
        'commentForm' : CommentForm(),
        'comments' : Comment.objects.filter(post = our_post.id )

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

        'posts': Post.objects.all(),
        'all_categories' : Category.objects.all(),
        'tittle' : "ALL You can read buffet",

    }

    return render(request, "blog/blog.html", context)


def postDetail(request):

    context = {
        'heading': 'Related Posts',
        'posts': ["I am number 4", "Wildlife", "Adventure"]

    }

    return render(request, 'blog/post-detail.html', context)

def saveComment (request,id):
    form =  CommentForm(request.POST)
    redirect_url ='/posts/details/'+id

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        message = form.cleaned_data['message']

        user = User.objects.get(pk = 1)
        post = Post.objects.get(pk =id)

        Comment.objects.create(message= message, user=user,post = post)

        return HttpResponseRedirect(redirect_url)

    else:

        return HttpResponseRedirect(redirect_url)


def dashboard(request):
    context = {

    }

    return render(request, 'blog/admin/dashboard.html', context)


def saveFeedback(request):

    name = request.POST.get("name",None)
    email = request.POST.get("email",None)
    phone_number = request.POST.get("number",None)
    message = request.POST.get("message",None)

    Feedback.objects.create(name=name, email=email,phone_number=phone_number, message=message)

    data = {}

    return JsonResponse(data)


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

def getCategoryPosts(request,id):

    category = Category.objects.get(pk =  id)
    posts = Post.objects.filter(Category= category.id)

    category.views += 1
    category.save()
    
    context = {
        'posts' : posts,
        'all_categories' : Category.objects.all(),
        'tittle' : "Posts in the category:"+category.name,
    }

    return render(request,'blog/blog.html',context)

def searchPost (request):

    search = request.POST.get('search',None)

    posts = Post.objects.filter(message__icontains=search).values()

    data ={
        'posts' :list(posts)
    }

    return JsonResponse(data)
   
def sendMail (request):
    if request.method =="POST":
        form = MailForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']

            send_mail(
                subject,
                message,
                'admin@gmail.com',
                [recipient],
                fail_silently = False
            )


            return HttpResponseRedirect('/staff/feedback')

    else:
        context ={
            'form' : MailForm
        }

        return render(request,'blog/admin/send_mail.html',context)



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
