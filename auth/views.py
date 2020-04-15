from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login


def registerView(requst):
    form = CreateUserForm()

    if requst.method == 'POST':
        form = CreateUserForm(requst.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(requst,'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}

    return render(requst, 'auth/register.html', context=context)


def loginView(requst):
    context = {}
    if requst.method == "POST":
        username = requst.POST.get('username')
        password = requst.POST.get('password')
        user = authenticate(requst, username=username, password=password)

        if user is not None:
            login(requst, user)
            return redirect('/')
        else:
            messages.info(requst, 'Username or password is incorrect')
            return render(requst, 'auth/login.html', context=context)

    return render(requst, 'auth/login.html', context=context)


def logoutUser(requst):
    logout(requst)
    return redirect('login')

