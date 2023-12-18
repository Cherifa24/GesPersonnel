from django.urls import path
from . import views
app_name='GesPerson'
urlpatterns = [ 
               path("accueil/",views.index,name='index'),
               path("add_person/",views.add_person,name='add_person'),
               path('add_teacher/',views.add_teacher, name='add_teacher'),
               path('add_student/',views.add_student, name='add_student'),
               path('teacher/', views.teacher_list, name='teacher_list'),
               path('student/', views.student_list, name='student_list'),
               path('teacher/update/<int:teacher_id>/',views.update_teacher, name='update_teacher'),
               path('student/update/<int:student_id>/',views.update_student, name='update_student'),
               path('display_person/', views.display_person, name='display_person'),
        ]