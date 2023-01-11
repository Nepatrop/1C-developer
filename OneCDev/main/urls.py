from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainCall),
    path('demand', views.demandCall),
    path('geography', views.geographyCall),
    path('skills', views.skillsCall),
    path('latestVacancies', views.latestVacanciesCall)
]