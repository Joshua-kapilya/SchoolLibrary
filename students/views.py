
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



from django.shortcuts import render, get_object_or_404
from .models import Student


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(
        request,
        "students/student_detail.html",
        {
            "student": student,
        },
    )



from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentCreateForm
from .models import Student, Grade

@login_required
def student_create(request, grade_name):
    grade = get_object_or_404(Grade, name=grade_name)

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(grade=grade)
            messages.success(request, "Student created successfully.")
            return redirect('students:grade_students', grade_name=grade.name)
    else:
        form = StudentCreateForm()

    return render(request, 'students/student_form.html', {'form': form, 'grade': grade})



@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('students:student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('students:student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})

