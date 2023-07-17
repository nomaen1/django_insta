from django.shortcuts import render, redirect
from .models import StatusModel, Posts

def index(request):
    status = StatusModel.objects.latest('id')
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        if title and image:
            try:
                status = StatusModel.objects.create(title=title, image=image)
                status.save()
                return redirect('index')
            except:
                return redirect('index')
        else:
            return redirect('profile')
    return render(request, "home.html", locals())

def posts(request):
    posts = Posts.objects.all()
    if request.method == "POST":
        description = request.POST.get('description')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        if description and location and image:
            try:
                posts = Posts.objects.create(description=description, location=location, image=image)
                posts.save()
                return redirect('index')
            except:
                posts = Posts.objects.create(description=description, location=location, image=image)
                posts.save()
                return redirect('index')
        else:
            return redirect('profile')
    return render(request, "home.html", locals())
                

def explore(request):
    return render(request, "explore.html")

def messages(request):
    return render(request, "messages.html")

