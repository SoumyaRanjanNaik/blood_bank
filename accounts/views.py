from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from accounts.models import UserDetail, Donation, DonationRequest

# Create your views here.


def accounts(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "account.html")


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            context["msg"] = "Invalid username or password"
            return render(request, "account.html", context)
    else:
        return


def register(request):
    context = {}
    if request.method == "POST":
        photo = request.FILES.get("photo")
        username = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        try:
            user = User.objects.create_user(username=username, password=password)
            details = UserDetail(
                user=user, photo=photo, name=name, mobile=mobile, address=address
            )
            details.save()
            login(request, user)
            print("complete")
            return redirect("dashboard")
        except IntegrityError:
            context["msg"] = "Already registered"
            return render(request, "account.html", context)
        except:
            context["msg"] = "Invalid data received"
            return render(request, "account.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("accounts")


@login_required
def dashboard(request):
    context = {"don": DonationRequest.objects.all()}
    return render(request, "dashboard.html", context)


def donate(request):
    i = request.POST.get("d_id")
    d = Donation(user=request.user, donation_for=DonationRequest.objects.get(id=i))
    d.save()
    context = {"msg": "Your response has been recorded"}
    return render(request, "confirm.html", context)
