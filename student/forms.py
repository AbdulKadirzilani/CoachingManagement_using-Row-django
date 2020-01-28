from django import forms
from .models import StudentProfile


class SearchStudentForm(forms.Form):
    roll = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    session = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


widgets ={

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control'}),
            'fathers_name' :forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.Textarea(attrs={'class': 'form-control'}),
            'session' : forms.TextInput(attrs={'class': 'form-control'}),
            'mobile' :forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields ='__all__'

