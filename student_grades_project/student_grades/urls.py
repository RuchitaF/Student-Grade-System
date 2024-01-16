# grades/urls.py
from django.urls import path
from .views import student_list
from .views import StudentDetailAPIView

app_name = 'student_grades'

urlpatterns = [
    path('students/', student_list, name='student_list'),
     path('students/<str:student_id>/', StudentDetailAPIView.as_view(), name='student_detail_api'),
]
