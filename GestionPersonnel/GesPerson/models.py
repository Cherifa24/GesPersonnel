from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    tel=models.IntegerField()
    email= models.EmailField(max_length=50)
    
    
    class Meta :
        abstract =True
    
    def __str__(self) -> str:
        return self.first_name + " "+ self.last_name +" " + str(self.tel) +" "+self.birth_date
        
        
class Teacher (Person) :
    speciality=models.CharField( max_length=50)

class Student(Person):
    pathway=models.CharField(max_length=50)