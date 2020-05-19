from django.urls import path
from accounts.views import *

urlpatterns = [
    path("", accounts, name="accounts"),
    path("login/", login_view, name="login"),
    path("register/", register, name="register"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("donate/", donate, name="donate"),
]
