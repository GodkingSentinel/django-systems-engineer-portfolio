from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("staff-dashboard/", views.staff_dashboard, name="staff_dashboard"),
    path(
        "download/recommendation-letter/",
        views.download_recommendation_letter,
        name="download_recommendation_letter",
    ),
]
