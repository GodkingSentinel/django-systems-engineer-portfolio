from django.shortcuts import render
from pathlib import Path
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404


def home(request):
    return render(request, "profilepage/home.html")


@login_required
def staff_dashboard(request):
    return render(request, "profilepage/staff_dashboard.html")


@login_required
def download_recommendation_letter(request):
    file_path = (
        Path(settings.BASE_DIR)
        / "profilepage"
        / "private_documents"
        / "Richard_Viens_Recommendation_Letter.pdf"
    )

    if not file_path.exists():
        raise Http404("Recommendation letter not found.")

    return FileResponse(
        open(file_path, "rb"),
        as_attachment=True,
        filename="Richard_Viens_Recommendation_Letter.pdf",
    )
