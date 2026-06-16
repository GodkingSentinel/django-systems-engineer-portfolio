from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "profilepage/home.html")


@login_required
def staff_dashboard(request):
    return render(request, "profilepage/staff_dashboard.html")

