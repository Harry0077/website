from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput)  # honeypot

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "topic", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@college.edu", "autocomplete": "email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone (optional)", "autocomplete": "tel"}),
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": "Tell us what you want to build and when you need it"}),
        }

    def clean_website(self):
        if self.cleaned_data.get("website"):
            raise forms.ValidationError("Spam detected.")
        return ""
