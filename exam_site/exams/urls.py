from django.urls import path
from . import views

urlpatterns = [
    path('kbexam/', views.exam_list, name='exam_list'),  # Замените mdexam на ваш префикс
]