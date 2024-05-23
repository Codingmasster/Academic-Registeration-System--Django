from django.shortcuts import render
from django.http import HttpResponse





def home(request):
    return render(request, "index.html")


def result_page(request):
    students = [
        {"name": "Hafiz Sibghat Ullah", 'gpa': 3.6},
        {"name": "Abis Hussain", 'gpa': 3.2},
        {"name": "Waqas Ahmed", 'gpa': 3.7},
        {"name": "Rashid Iqbal", 'gpa': 2.8},
        {"name": "Wardah Tariq", 'gpa': 3.3},
    ]
    friends = ['Sibghat Ullah','Rehman Baba','Awais Gujjar','Waqas Ahmed','Abis Hussain']
    
    return render(request, "result.html",context={'std_data':students,'friends': friends})

def about_page(request):
    return render(request, "about.html")