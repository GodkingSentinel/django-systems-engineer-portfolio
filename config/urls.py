from django.contrib import admin
from django.urls import path, include
from profilepage import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("staff/", views.staff_dashboard, name="staff_dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
]