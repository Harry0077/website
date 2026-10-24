from django.db import models


class Project(models.Model):
    IOT, WEB = "iot", "web"
    CATEGORIES = [(IOT, "IoT project"), (WEB, "Website build")]

    category = models.CharField(max_length=3, choices=CATEGORIES)
    title = models.CharField(max_length=120)
    summary = models.TextField(help_text="2-3 lines shown on the card")
    tech = models.CharField(max_length=200, help_text="Comma separated, e.g. ESP32, MQTT, Django")
    image = models.ImageField(upload_to="projects/", blank=True)
    link = models.URLField(blank=True, help_text="Demo or GitHub link (optional)")
    featured = models.BooleanField(default=False, help_text="Show on the home page")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created"]

    def __str__(self):
        return f"{self.get_category_display()}: {self.title}"

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech.split(",") if t.strip()]


class ContactMessage(models.Model):
    TOPICS = [("iot", "IoT project"), ("web", "Website"), ("other", "Something else")]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    topic = models.CharField(max_length=5, choices=TOPICS, default="iot")
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.get_topic_display()})"
