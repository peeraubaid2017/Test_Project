from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import EmployeeData,Register,CustomUser
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def home(request):
    return render(request,'template.html')

# @login_required(login_url='employee_login')
# @user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists())
# def details(request):
#     if request.method == 'GET':
#         name = request.GET.get('searchname', '')
#         start_date = request.GET.get('fromdate', '')
#         end_date = request.GET.get('to', '')
#         val_1={'name':name,'fromdate':start_date,'to':end_date}
#         data_1 = EmployeeData.objects.all()
#         if name:
#             data_1 = data_1.filter(name__icontains=name)
#         if start_date:
#             data_1 = data_1.filter(date__gte=start_date)
#         if end_date:
#             data_1 = data_1.filter(date__lte=end_date)
#         paginator = Paginator(data_1, 10)
#         page_number = request.GET.get('page')
#         data_1 = paginator.get_page(page_number)
#         return render(request, 'index.html', {'data_1':data_1,'val_1':val_1})
#     data_1 = EmployeeData.objects.all()
#     return render(request, 'index.html',{'data_1':data_1})



def employee_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard') # Replace 'home' with your desired URL name
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')




# @user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show')
def guidelines(request):
    return render(request,'typography.html')



# def employee_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('uname')
#         password = request.POST.get('pwd')
#         user = authenticate(username=username, password=password)
#         val={'username':username}
#         error_Msg=''
#         if (not username):
#             error_Msg="User name is Required"
#         elif (not password):
#             error_Msg="Password is Required"
#         elif user is None:
#             error_Msg="Incorrect Username/Password"
#         if user is not None:
#             login(request,user) 
#             messages.success(request, "Successfully Logged In")
#             return redirect('dashboard')
#         else:
#             data={
#                 'error_message': error_Msg,
#                 'vals':val
#                 }
#             return render(request, 'login.html', data)
#     return render(request, 'login.html')


@login_required(login_url='employee_login')
@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show')
def edit(request):
    emp_id=request.GET['id']   
    for data in EmployeeData.objects.filter(emp_id=emp_id):
        name=data.name
        date=data.date
        check_in=data.check_in
        check_out=data.check_out
    return render(request,"edit.html",{'emp_id':emp_id,'name':name,'date':date,'check_in':check_in,'check_out':check_out})

@login_required(login_url='employee_login')
@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show')
def RecordEdited(request):
    if request.method == 'POST':
        emp_id=request.POST['empid']
        name=request.POST['empname']
        date=request.POST['date']
        check_in=request.POST['checkin']
        check_out=request.POST['checkout']
        EmployeeData.objects.filter(emp_id=emp_id).update(name=name,date=date,check_in=check_in,check_out=check_out)
        return HttpResponseRedirect("dashboard")


@login_required(login_url='employee_login')
@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show')
def delete(request,pk):
    emp=EmployeeData.objects.get(pk=pk)
    if request.method == "POST":
        emp.delete()
        return redirect('dashboard')
    context = {'emp': emp}
    return render(request,'delete.html',context)

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        myuser = CustomUser.objects.create_user(email, password, is_staff = False, is_active = True)
        myuser.save()
        return redirect('employee_login')
    # else:
    #     val={
    #         # 'error':errorMsg,
    #         'values':value
    #     }
        # return render(request,'register.html',val)
    return render(request,'register.html')




# def register(request):
#     if request.method =='POST':
#         postdata=request.POST
#         email = postdata.get('email')
#         password = postdata.get('password')
#         confirm_password = postdata.get('confirm_password')
        

#         errorMsg=''
#         if password != confirm_password:
#             errorMsg="password do not match"
#         if not errorMsg:
#             form = Register( email=email, password=password, confirm_password=confirm_password)
#             form.save()
            
#             return redirect('employee_login')
#         else:
#             val={
#                 'error':errorMsg,
                
#             }
#             return render(request,'register.html',val)
#     return render(request,'register.html')


def login_user(request):
    # toggle_switch = ToggleSwitch.objects.all()
    # if request.method == 'POST':
    #     if not toggle_switch.is_on:
    #         messages.error(request, 'Login is disabled')
    #         return redirect('login_user')
    #     # handle form submission and authenticate user
    #     context = {'toggle_switch': toggle_switch}
    #     return render(request, 'check.html', context)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password= request.POST.get('password')
        x = Register.objects.all().filter(email = email, username = username, password = password)        
        for i in x:
          if i.email == email and i.username == username and i.password == password:
              return render(request, 'check.html')    
    return render(request, 'user_login.html')


@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show')
def newuser(request):
    data = CustomUser.objects.all()
    return render(request,'newuser.html',{'data_2':data})

def dashboard(request):
    return render(request, 'dashboard.html')

    # dashboarddata=EmployeeData.objects.all()
    # return render(request, 'dashboard.html',{'data_1':dashboarddata})



# def login_view(request):
#     toggle_switch = ToggleSwitch.objects.first()
#     if request.method == 'POST':
#         if not toggle_switch.is_on:
#             messages.error(request, 'Login is disabled')
#             return redirect('login_user')
#         # handle form submission and authenticate user
#     context = {'toggle_switch': toggle_switch}
#     return render(request, 'check.html', context)



def template(request):
    return render(request,'template.html')


def show(request):
    return render(request, 'show.html')



@user_passes_test(lambda u: u.groups.filter(name='SuperUser').exists(),login_url='show')
def export(request):
    if request.method == 'GET':
        name = request.GET.get('searchname')
        # start_date = request.GET.get('fromdate', '')
        # end_date = request.GET.get('to', '')
        # val_1={'name':name,'fromdate':start_date,'to':end_date}
        data_1 = EmployeeData.objects.all()
        if name:
            data_1 = data_1.filter(name__icontains=name)
        # if start_date:
            # data_1 = data_1.filter(date__gte=start_date)
        # if end_date:
            # data_1 = data_1.filter(date__lte=end_date)
        paginator = Paginator(data_1, 5)
        page_number = request.GET.get('page')
        data_1 = paginator.get_page(page_number)
        return render(request, 'export.html', {'data_1':data_1})
    data_1 = EmployeeData.objects.all()
    return render(request, 'export.html',{'data_1':data_1})
    # return render(request, 'export.html')