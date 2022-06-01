from django import forms
from employer.models import Jobs
# class JobForm(forms.Form):
#     job_title=forms.CharField()
#     company_name=forms.CharField()
#     location=forms.CharField()
#     salary=forms.IntegerField()
#     experience=forms.IntegerField()
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = "__all__"
        #OR exclude = ['salary'] for exclude only salary

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2","first_name","last_name"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


