from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add_student(request):

    if request.method == 'POST':

        name = request.POST['name']
        roll = request.POST['roll']
        course = request.POST['course']
        email = request.POST['email']

        Student.objects.create(
            name=name,
            roll=roll,
            course=course,
            email=email
        )

        return redirect('/')

    return render(request, 'add.html')

def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect('/')