from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Specialization, Area, Doctor


def home(request):
    specializations = Specialization.objects.all()
    areas = Area.objects.all()
    return render(request, 'home.html', {'specializations': specializations, 'areas': areas})

@login_required
def search(request):
    specialization = request.GET.get('specialization')
    area = request.GET.get('area')
    doctors = Doctor.objects.filter(specialization__name=specialization, area__name=area)
    return render(request, 'search.html', {'doctors': doctors})

@login_required
def doctor_info(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'doctors_info.html', {'doctor': doctor})

