from django.http import HttpResponse
from .models import Creator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm


def home(request):
    #return HttpResponse('Привіт це мій перший views!')
    return render(request, 'home.html')

def creators(request):
    creators_obj = Creator.objects.all()
    #return HttpResponse(creators_obj)
    context = {'creators': creators_obj}
    return render(request, 'creators.html', context)

def creator(request, pk):
    creators_obj = Creator.objects.filter(id=pk).first()
    #return HttpResponse(creators_obj)
    context = {'creator': creators_obj}
    return render(request, 'creator.html', context)

def info_view(request):
    return render(request, 'info.html')

def videos(request):
    return render(request, 'videos.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('school:login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('store:store-home')  # змінити на вашу сторінку
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Невірний логін або пароль'
                })
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('store:login')