from django.shortcuts import render ,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def index(request):

    return  render(request,'index.html', {})



def add_person(request):
    return render(request,'add_person.html', locals())

#########################""view de teacher
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.cleaned_data
            form.save()
           
            return redirect('GesPerson:teacher_list') 
    else:
        form = TeacherForm()

    return render(request,'teachers/add_teacher.html', {'form': form})


def teacher_list(request):
    teachers= Teacher.objects.all()
    return render(request,'teachers/teacher_list.html', locals())

def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(reverse('GesPerson:teacher_list'))
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'teachers/teacher_update.html', locals())


#################view students
def add_student(request):
    if request.method == 'POST':
      
        form = StudentForm(request.POST)
        
        if form.is_valid():
           
            form.save()
            return redirect('GesPerson:student_list')  
    else:
     
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})


def student_list(request):
    students= Student.objects.all()
    return render(request,'students/student_list.html', locals())

##update for student
def update_student(request,  student_id):
    student= get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('GesPerson:student_list'))
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_update.html', locals())


####
def display_person(request):
      
      return render(request,'display_person.html', locals())
    