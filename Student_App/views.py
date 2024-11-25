from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student_view(request):
    return HttpResponse('we are student')