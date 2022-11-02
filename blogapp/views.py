from django.shortcuts import render,redirect, HttpResponse
from .models import blog

# Create your views here.
def browse(req):

    blg = blog.objects.all()
    context = {"blg": blg}
    return render(req, "browse.html", context)


def viewblog(req):
    id = req.GET["blogid"]
    blg = blog.objects.get(id=id)
    context = {"blog": blg}
    return render(req, "viewblog.html", context)


def createblog(req):
    context = {}
    return render(req, "createblogs.html", context)


def submitblog(req):
    title = req.GET["title"]
    text = req.GET["text"]
    author = req.GET["author"]
    blog.objects.create(title=title, text=text, author=author)
    return redirect('/blog/browse')
