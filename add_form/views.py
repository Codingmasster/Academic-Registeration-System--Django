from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout
# Create your views here.
def Addmission_form(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        name=data.get("name")
        email=data.get("email")
        class_name=data.get("class_name")
        subject=data.get("subject")
        image=request.FILES.get("image")
        file=request.FILES.get("file")
        Student.objects.create(name=name, email=email, class_name=class_name, subject=subject , image=image, file=file)
        # Student.objects.create(name=name, email=email, class_name=class_name, subject=subject , image=image, file=file)
        print(name, email, class_name, subject, image, file, sep=" ")
    return render(request, "Addmission_form.html")

def show_data(request):
    data = Student.objects.all()
    if request.GET.get('search'):
        data=data.filter(name__icontains=request.GET.get('search'))
    context={'Students': data}
    return render(request,"students_data.html",context)

def delete_data(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('http://127.0.0.1:8000/show_data/')

def update_data(request,id):
    student_data = Student.objects.get(id=id)
    context = {'std':student_data}
    if request.method == 'POST':
        data = request.POST
        print(data)
        student_data.name=data.get("name")
        student_data.email=data.get("email")
        student_data.class_name=data.get("class_name")
        student_data.subject=data.get("subject")
        student_data.image=request.FILES.get("image")
        student_data.save()
        return redirect('http://127.0.0.1:8000/show_data/')
    else :
        print("No getting any data")
    return render(request,"update_data.html",context)

def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Error: Username don't exist")
            return redirect("http://127.0.0.1:8000/")
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Error: Your password is incorrect")
            return redirect("http://127.0.0.1:8000/")
        else:
            login(request,user)
            return redirect("http://127.0.0.1:8000/home/")
      
    return render(request,"login.html")

def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Error: Username already existed")
            return redirect("http://127.0.0.1:8000/sign_up/")
        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()
        return redirect("http://127.0.0.1:8000/")
      
    return render(request,"sign_up.html")

def log_out(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")
