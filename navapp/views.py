from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def services(request):
    return render(request,'services.html')
def aboutus(request):
    return render(request,'aboutus.html')
def contact(request):
    return render(request,'contact.html')