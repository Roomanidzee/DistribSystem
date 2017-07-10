from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    
    username = forms.CharField(max_length = 50, label = "Имя пользователя")
    lastname = forms.CharField(max_length = 50, required = True, label = "Фамилия")
    firstname = forms.CharField(max_length = 50, required = True, label = "Имя")    
    patronymic = forms.CharField(max_length = 50, required = True, label = "Отчество") 
    
    email = forms.EmailField(widget = forms.EmailInput, label = "Электронная почта")
    pass1 = forms.CharField(widget = forms.PasswordInput, label = "Пароль")
    pass2 = forms.CharField(widget = forms.PasswordInput, label = "Повторите пароль")
    
    def clean_pass2(self):
        
        if(self.cleaned_data["pass2"] != self.cleaned_data.get("pass1", "")):
            
            raise forms.ValidationError("Пароли не свопадают")  
        
        return self.cleaned_data["pass2"]
    
class UserProfileForm(forms.ModelForm):
    
    type = forms.ChoiceField(widget = forms.Select, label = "Должность")        