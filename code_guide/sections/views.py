# sections/views.py
from django.shortcuts import render
from .models import Section

def home(request):
    # Fetch all sections from the database
    sections = Section.objects.all()
    return render(request, 'sections/home.html', {'sections': sections})

def section_detail(request, section_id):
    # Fetch a specific section by its ID and its subsections
    section = Section.objects.get(id=section_id)
    subsections = section.subsections.all()  # Get related sub-sections
    return render(request, 'sections/section_detail.html', {'section': section, 'subsections': subsections})
