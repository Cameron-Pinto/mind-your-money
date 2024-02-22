from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.template import loader
# from .models import Post

# Create your views here.


@login_required(login_url="/login")
def home(request):
    return render(request, "pathways/home.html")


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})


@login_required(login_url="/login")
def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="/login")
def dashboard(request):
    return render(request, "pathways/dashboard.html")
