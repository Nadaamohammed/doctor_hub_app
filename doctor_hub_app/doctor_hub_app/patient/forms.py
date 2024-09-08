from django import forms
from .models import Patients

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['Patient_Name', 'Patient_Email', 'Patient_Password']
        widgets = {
            'Patient_Password': forms.PasswordInput(),
        }
