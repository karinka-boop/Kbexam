from django.shortcuts import render
from .models import Kbexam  # Замените на вашу модель

def exam_list(request):
    exams = Kbexam.objects.filter(is_public=True)  # Замените на вашу модель
    return render(request, 'exams/exam_list.html', {'exams': exams})
# Create your views here.
