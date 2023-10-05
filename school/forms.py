from datetime import timezone

from django import forms
from django.core.exceptions import ValidationError

from .models import Teacher
from .models import Group


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "birth_date", "subject"]

    def clean_birthdate(self):
        birthdate = self.cleaned_data["birth_date"]
        if birthdate > timezone.now().date():
            raise ValidationError("Дата народження не може бути в майбутньому.")
        return birthdate


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "curator"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if Group.objects.filter(name=name).exists():
            raise ValidationError("Група з таким ім'ям вже існує.")
        return name
