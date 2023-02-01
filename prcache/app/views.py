from django.shortcuts import render

def home(reqeust):
    return render(reqeust,'home.html')
