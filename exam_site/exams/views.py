from django.shortcuts import render
from .models import kbexam

def exam_list(request):
    exams = kbexam.objects.filter(is_public=True)
    return render(request, 'exams/exam_list.html', {
        'exams': exams,
        'full_name': 'Баймухамедова Карина Ренатовна',
        'group_number': '241-671'
    })

