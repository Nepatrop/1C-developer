from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainCall(request):
    return render(request, 'main/index.html')

def demandCall(request):
    return render(request, 'main/demand.html')

def geographyCall(request):
    return render(request, 'main/geography.html')

def skillsCall(request):
    return render(request, 'main/skills.html')

def latestVacanciesCall(request):
    return render(request, 'main/latestVacancies.html')