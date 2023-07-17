from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.users.models import User

def user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if password and username and email:
            try:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                authenticated_user = authenticate(request, username=username, password=password)
                if authenticated_user:
                    login(request, authenticated_user)
                    return redirect('status')
                else:
                    return redirect('register')
            except:
                return redirect('status')
        else:
            return redirect('register')
    return render(request, "form-register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValueError('Пользователь с такой почтой не существует.')
            return redirect("login")
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("status")
        else:
            raise ValueError('Неправильный пароль.')
            return redirect("login")
        

    return render(request, 'form-login.html', locals())

def profile(request):
    return render(request, "profile.html")