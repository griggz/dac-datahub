from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email").lower()
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")

    return render(request, "accounts/login_form.html", {"form": form, "title": title})


def register_view(request):
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password2")
        email = form.cleaned_data.get("email")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        user.set_password(password)
        user.is_active = False
        user.save()

        # Email New User
        # email_new_user.delay(email, first_name)

        # Email Admins
        # email_admins.delay(email, first_name, last_name)

        messages.success(request, "Thank you for registering! Your request is now being reviewed. You will receive a notification once approved.")

        if next:
            return redirect(next)
        return redirect('/account/login')

    context = {
        "form": form,
        "title": title
    }
    return render(request, "accounts/register_form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/account/login")
