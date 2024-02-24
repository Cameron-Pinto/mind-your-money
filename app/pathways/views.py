from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.template import loader
# from .models import Post

# Create your views here.


def home(request):
    return render(request, "pathways/home.html")


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("two_factor:login")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})


@login_required(login_url="two_factor:login")
def logout_view(request):
    logout(request)
    return redirect("home")


@login_required(login_url="two_factor:login")
def dashboard(request):
    return render(request, "pathways/dashboard.html")


@login_required(login_url="two_factor:login")
def settings_view(request):
    return render(request, "settings/user_settings.html")


@login_required(login_url="two_factor:login")
def security_view(request):
    return render(request, "settings/security_view.html")
