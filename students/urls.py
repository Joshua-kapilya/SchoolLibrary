from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("grades/", views.grade_list, name="grade_list"),
    path('grade/<str:grade_name>/', views.grade_students, name='grade_students'),
]
