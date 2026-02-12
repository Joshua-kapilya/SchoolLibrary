from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("grades/", views.grade_list, name="grade_list"),
    path('grade/<str:grade_name>/', views.grade_students, name='grade_students'),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path('add/<str:grade_name>/', views.student_create, name='student_add'),
    path('<int:pk>/edit/', views.student_update, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
]
