from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from schoolapp.forms import PersonCreationForm
from schoolapp.models import Department, Person, Course


# Create your views here.
def index(request):
    return render(request,'core/index.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return render(request, 'accounts/user_login.html')

    return render(request,'accounts/user_login.html')

def register(request):
    if request.method =='POST':
        username = request.POST.get['uname']
        password = request.POST.get['psw']
        cpassword = request.POST.get['psw_repeat']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already taken')
                return render(request,"accounts/user_registration.html")
            else:
                user = User.objects.create_user(username=username,password=password)

                user.save();
                print("user created")
                messages.info(request, 'account created')
                return render(request,'accounts/user_login.html')

        else:
            messages.info(request,"password not matching")
            print("password not matching")
            return redirect("register")
        return redirect("/")
    return render(request, "accounts/user_registration.html")

def logout(request):
    auth.logout(request)
    return  redirect("/")
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Order placed successfully')
            return redirect('/')

    return render(request, 'accounts/home.html', {'form': form})
def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'accounts/home.html', {'form': form})


# AJAX
def load_cities(request):
    departnent_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=departnent_id).all()
    return render(request, 'accounts/city_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(courses.values('id', 'name')), safe=False)


