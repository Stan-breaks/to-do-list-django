from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'list/index.html')

def register(request):
    if request.method!='POST':
        return render(request,'list/register.html')

def login(request):
    pass
def logout(request):
    pass