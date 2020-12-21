from django.urls import path
from . import views


urlpatterns = [
    path('', views.currentpathway, name ='SEAS_Course_Planner-currentpathway'),
    path('newpathway/', views.newpathway, name ='SEAS_Course_Planner-newpathway'),
]