
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def grade_list(request):
    return render(request, "students/grade_list.html")


from django.shortcuts import render, get_object_or_404
from .models import Student, Grade
from datetime import date

def grade_students(request, grade_name):
    # Fetch grade ignoring case and extra spaces
    grade = get_object_or_404(Grade, name__iexact=grade_name.strip())

    students = Student.objects.filter(grade=grade)

    for student in students:
        if student.profile.date_of_birth:
            today = date.today()
            student.age = today.year - student.profile.date_of_birth.year - (
                (today.month, today.day) < (student.profile.date_of_birth.month, student.profile.date_of_birth.day)
            )
        else:
            student.age = "N/A"

    context = {
        'grade_name': grade.name,
        'students': students,
    }
    return render(request, 'students/grade_students.html', context)
