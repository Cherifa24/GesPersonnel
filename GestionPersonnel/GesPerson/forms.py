from django import forms
from GesPerson.models import *
#Avec la classe Form , d'apres mes recherche dans la documentation, j'ai pas trouvée la methode de form pour enregistrer les données du formulaire
# class TeacherForm(forms.Form):
#       first_name=forms.CharField(label="first_name",max_length=50, required=True)
#       last_name=forms.CharField(label="Last Name", max_length=50, required=True)
#       birth_date=forms.DateField(label="Birthday Date", required=True)
#       tel=forms.IntegerField(label="Phone Number", required=False)
#       email=forms.EmailField(label="E-mail", required=False)
#       speciality=forms.CharField(label="Speciality", max_length=50, required=False)
      
      
class TeacherForm(forms.ModelForm):
    class Meta :
        model=Teacher
        fields="__all__"
        
    def clean(self):
        
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name.isalpha():
       
            raise forms.ValidationError("le champs first_name n'accepte pas les caractères numériques.")
        if not last_name.isalpha():
            raise forms.ValidationError("le champs last_name n'accepte pas les caractères numériques.")
        

        return cleaned_data
    
class StudentForm(forms.ModelForm):
    class Meta :
        model=Student
        fields="__all__"
        
    def clean(self):
        
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name.isalpha():
       
            raise forms.ValidationError("le champs first_name  n'accepte pas les caractères numériques.")
        if not last_name.isalpha():
            raise forms.ValidationError("le champs last_name  n'accepte pas les caractères numériques.")
        

        return cleaned_data