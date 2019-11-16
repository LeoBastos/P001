from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # validação senha igual
        if password == password2:
            # validar username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Esse Usuário já existe')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email já Cadastrado')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name)
                    # auth.login(request, user)
                    # messages.success(request, 'Usuário Cadastrado com Sucesso')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Usuário Cadastrado com Sucesso')
                    return redirect('login')
        else:
            messages.error(request, 'As Senhas não combinam')
            return redirect('register')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Seja Bem Vindo(a)')
            return redirect('dashboard')

        else:
            messages.error(request, 'Credenciais Inválidas')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # validação senha igual
        if password == password2:
            # validar username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Esse Usuário já existe')
                return redirect('profile')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email já Cadastrado')
                    return redirect('profile')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name)
                    # auth.login(request, user)
                    # messages.success(request, 'Usuário Cadastrado com Sucesso')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Usuário Cadastrado com Sucesso')
                    return redirect('profile')
        else:
            messages.error(request, 'As Senhas não combinam')
            return redirect('profile')
        return redirect('profile')
    else:
        return render(request, 'accounts/profile.html')