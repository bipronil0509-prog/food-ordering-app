from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    context = {
        "x":"Bipro",
        "var2":"Bip",
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse("About")
def services(request):
    return HttpResponse("services")
def contact(request):
    return HttpResponse("Contact")