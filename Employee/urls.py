from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("employee_login",views.employee_login,name='employee_login'),
    path("details",views.details,name='details'),
    path("edit", views.edit, name='edit'), 
    path("register", views.register, name='register'), 
    path("guidelines", views.guidelines, name='guidelines'), 
    path("newuser", views.newuser, name='newuser'), 
    path("login_user", views.login_user, name='login_user'), 
    # path("login_view", views.login_view, name='login_view'), 
    path('RecordEdited',views.RecordEdited, name='RecordEdited'),
    path("delete/<int:pk>",views.delete,name='delete'),
    path("dashboard",views.dashboard, name='dashboard')
]