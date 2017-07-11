from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    username = forms.CharField(max_length=50, label="Имя пользователя")
    last_name = forms.CharField(max_length=50, required=True, label="Фамилия")
    first_name = forms.CharField(max_length=50, required=True, label="Имя")
    
    email = forms.EmailField(widget=forms.EmailInput, label="Электронная почта")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    pass2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
    
    def __clean_pass2__(self):
        
        if self.cleaned_data["pass2"] != self.cleaned_data.get("password", ""):
            
            raise forms.ValidationError("Пароли не совпадают")  
        
        return self.cleaned_data["pass2"]
        fields = ['patronymic', 'sex']