from django.shortcuts import render, HttpResponse

# Create your views here.
def index(requests):
    context={
        "variable":"this is sent"
    }
    return render(requests, 'index.html',context)

def about(requests):
    return HttpResponse("This is about page")

def services(requests):
    return HttpResponse("This is services page")

def contact(requests):
    return HttpResponse("This is contact page")