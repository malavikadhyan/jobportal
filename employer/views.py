from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView,TemplateView
from employer.forms import JobForm,SignUpForm,LoginForm
from employer.models import Jobs
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

#list,detail,update,delete
class EmployerHomeView(View):
    def get(self,request):
        return render(request,"home.html")

class AddJobViews(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-addjob.html"
    success_url = reverse_lazy("emp-alljob")   #used in post cases
""" def get(self,request):
        form=JobForm()
        return render(request,"emp-addjob.html",{"form":form})
    def post(self,request):
        form=JobForm(request.POST)
        if form.is_valid():
            # jobname=form.cleaned_data.get("job_title")
            # cname=form.cleaned_data.get("company_name")
            # loc=form.cleaned_data.get("location")
            # salary=form.cleaned_data.get("salary")
            # exp=form.cleaned_data.get("experience")
            # Jobs.objects.create(
            #     job_title=jobname,
            #     company_name=cname,
            #     location=loc,
            #     salary=salary,
            #     experience=exp,
            # )
            form.save()
            return render(request,"home.html")
        else:
            return render(request,"emp-addjob.html",{"form":form}) """

class ListJobViews(ListView):
    # def get(self,request):
    #     qs=Jobs.objects.all()
    #     return render(request,"emp-listjob.html",{"jobs":qs})
    #use variables as same as class ListView
    model=Jobs
    context_object_name="jobs"
    template_name="emp-listjob.html"

class JobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "emp-detailjob.html"
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailjob.html",{"job":qs})

class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-editjob.html"
    success_url = reverse_lazy("emp-alljob")
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     return render(request,"emp-editjob.html",{"form":form})
    # def post(self,request,id):
    #     qs = Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("emp-alljob")
    #     else:
    #         return render(request,"emp-editjob.html",{"form":form})
class JobDeleteView(DeleteView):
    template_name = "emp-deletejob.html"
    success_url = reverse_lazy("emp-alljob")
    pk_url_kwarg = "id"
    model = Jobs
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect("emp-alljob")
class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "usersignup.html"
    success_url = reverse_lazy("emp-alljob")

class SignInView(FormView):
    form_class=LoginForm
    template_name = "login.html"
    model=User
    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            un=form.cleaned_data.get("username")
            pw=form.cleaned_data.get("password")
            user=authenticate(request,username=un,password=pw)
            if user:
                login(request,user)
                return redirect("emp-home")
            else:
                return render(request,"login.html",{"form":form})
def signout_view(request,*args,**kwargs):

    logout(request)
    return redirect("signin")

class ChangePasswordView(TemplateView):
    template_name = "changepassword.html"

    def post(self,request,*args,**kwargs):
        pwd=request.POST.get("pwd")
        uname=request.user
        user=authenticate(request,username=uname,password=pwd)
        if user:
            return redirect("password-reset")
        else:
            return render(request,self.template_name)

class PasswordResetView(TemplateView):
    template_name = "passwordreset.html"
    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2=request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{"msg":"password mismatch"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")