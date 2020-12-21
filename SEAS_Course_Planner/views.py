from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def currentpathway(request):

	return render(request, "SEAS_Course_Planner/home.html")
@login_required
def newpathway(request):
	return render(request, "SEAS_Course_Planner/newpathway.html")