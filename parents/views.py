from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from students.models import Grade, Student
from parents.models import Parent


@login_required
def parent_grade_list(request):
    """
    Show all grades so the admin can select a grade to see its parents.
    """
    grades = Grade.objects.all()
    return render(
        request,
        "parents/parent_grade_list.html",
        {"grades": grades}
    )


@login_required
def parents_in_grade(request, grade_id):
    """
    Show all parents who have students in a specific grade.
    """
    grade = get_object_or_404(Grade, id=grade_id)

    # Get all Parent objects linked to students in this grade
    parents = Parent.objects.filter(
        children__grade=grade
    ).distinct()

    # Prefetch related students to avoid N+1 queries
    parents = parents.prefetch_related(
        "children__profile"
    )

    return render(
        request,
        "parents/parents_in_grade.html",
        {
            "grade": grade,
            "parents": parents,
        }
    )


@login_required
def parent_detail(request, parent_id):
    """
    Show details of a single parent, including their students.
    """
    parent = get_object_or_404(
        Parent,
        id=parent_id
    )

    # Get all students linked to this parent
    students = parent.children.select_related("grade", "profile").all()

    return render(
        request,
        "parents/parent_detail.html",
        {
            "parent": parent,
            "students": students,
        }
    )

