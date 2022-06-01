from django.urls import path
from employer import views
urlpatterns = [
   path('home',views.EmployerHomeView.as_view(),name="emp-home"),
   path('job/add',views.AddJobViews.as_view(),name="emp-addjob"),
   path('job/all',views.ListJobViews.as_view(),name="emp-alljob"),
   path('job/detail/<int:id>',views.JobDetailView.as_view(),name="emp-jobdetail"),
   path('job/change/<int:id>',views.JobEditView.as_view(),name="emp-editjob"),
   path('job/remove/<int:id>',views.JobDeleteView.as_view(),name="emp-deletejob"),
   path('users/account/signup',views.SignUpView.as_view(),name="signup"),
   path('users/account/login',views.SignInView.as_view(),name="signin"),
   path('users/account/signout',views.signout_view,name="signout"),
   path('users/password/change',views.ChangePasswordView.as_view(),name="password-change"),
   path('users/password/reset',views.PasswordResetView.as_view(),name="password-reset"),
]
