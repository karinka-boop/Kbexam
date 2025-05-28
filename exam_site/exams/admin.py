from django.contrib import admin
from .models import kbexam

class kbexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title', 'users__email')
    date_hierarchy = 'exam_date'
    filter_horizontal = ('users',)  # Для удобного выбора студентов

admin.site.register(kbexam, kbexamAdmin)
