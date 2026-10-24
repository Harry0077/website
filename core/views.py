from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Project


def home(request):
    featured = Project.objects.filter(featured=True)[:6]
    return render(request, "core/home.html", {
        "featured": featured,
        "iot_count": Project.objects.filter(category="iot").count(),
        "web_count": Project.objects.filter(category="web").count(),
    })


def about(request):
    return render(request, "core/about.html")


def iot_projects(request):
    return render(request, "core/projects.html", {
        "projects": Project.objects.filter(category="iot"),
        "kind": "iot",
        "title": "IoT projects",
        "intro": "Sensors, microcontrollers and dashboards that work on the bench and in your viva.",
    })


def web_builds(request):
    return render(request, "core/projects.html", {
        "projects": Project.objects.filter(category="web"),
        "kind": "web",
        "title": "Website builds",
        "intro": "Fast, responsive sites for students, clubs and small businesses.",
    })


def contact(request):
    topic = request.GET.get("topic")
    form = ContactForm(request.POST or None, initial={"topic": topic} if topic else None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Message sent. We will reply within one working day.")
        return redirect("contact")
    return render(request, "core/contact.html", {"form": form})
