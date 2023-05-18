from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.forms import LoginForm, AddUserForm
from django.views import View

# Create your views here.


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'book_generic/form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect('index')
        return render(request, 'book_generic/form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class AddUserView(View):

    def get(self, request):
        form = AddUserForm()
        return render(request, 'book_generic/form.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('index')
        return render(request, 'book_generic/form.html', {'form': form})
