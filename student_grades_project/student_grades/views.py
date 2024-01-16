# Inside student_grades_app/views.py
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

def calculate_average_grade(student):
    grades = [float(grade[:-1]) for grade in [student.module1_grade, student.module2_grade, student.module3_grade]]
    return sum(grades) / len(grades)

def classify_result(average):
    return "Distinction" if average >= 70 else "Merit" if average >= 60 else "Pass" if average >= 40 else "Fail"

def update_student_results(students):
    for student in students:
        average = calculate_average_grade(student)
        student.result, student.average_grade = classify_result(average), average

def student_list(request):
    students = Student.objects.all()
    update_student_results(students)
    context = {'students': students}
    return render(request, 'student_grades/student_list.html', context)

class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'

    def calculate_result(self, student):
        grades = [int(grade[:-1]) for grade in [student.module1_grade, student.module2_grade, student.module3_grade]]
        average_grade = sum(grades) / len(grades)
        return classify_result(average_grade)

    def update_student_results(self, students):
        update_student_results(students)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.update_student_results([instance])  # Call the method to update results
        data = serializer.data
        data['result'] = self.calculate_result(instance)
        return Response(data)

def index(request):
    return render(request, 'student_grades/index.html')
