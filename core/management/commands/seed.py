from django.core.management.base import BaseCommand
from core.models import Project

DATA = [
    ("iot", "Smart attendance tracker", "RFID cards log attendance to a live dashboard. Teachers export a CSV at the end of the week.", "ESP32, RFID, MQTT, Django", True),
    ("iot", "Soil moisture and auto irrigation", "Reads soil moisture and switches a pump on when the field is dry. Alerts you on your phone.", "Arduino, Sensors, Relay, Blynk", True),
    ("iot", "Home energy monitor", "Measures power per appliance and plots daily usage so you can see where units go.", "ESP8266, CT sensor, InfluxDB, Grafana", False),
    ("iot", "Gas leak and fire alert", "Detects gas or smoke, sounds a buzzer and sends an SMS to saved numbers.", "Arduino, MQ-2, GSM, Buzzer", False),
    ("web", "College club website", "Events, member list and a registration form that stores entries in a database.", "Django, PostgreSQL, Tailwind", True),
    ("web", "Local shop catalogue", "A mobile-first product catalogue with WhatsApp order buttons.", "Django, HTML, CSS, JavaScript", True),
    ("web", "Portfolio for students", "A clean one-page portfolio with projects, resume download and contact form.", "HTML, CSS, JavaScript", False),
]

class Command(BaseCommand):
    help = "Add sample projects so the pages are not empty"

    def handle(self, *args, **opts):
        if Project.objects.exists():
            self.stdout.write("Projects already exist. Skipping.")
            return
        for cat, title, summary, tech, feat in DATA:
            Project.objects.create(category=cat, title=title, summary=summary, tech=tech, featured=feat)
        self.stdout.write(self.style.SUCCESS(f"Added {len(DATA)} sample projects."))
