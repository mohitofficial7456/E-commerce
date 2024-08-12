from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signup(request):
    print("Signup Function called")
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirm_password = request.POST.get("pass2")
        if password != confirm_password:
            messages.warning(request,"Password not matching")
            return render(request,"authentication/signup.html")

        try:
            if User.objects.get(username = email):
                return HttpResponse("User alreay exists")
        
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email,email,password)
        user.save()
        return render(request,"authentication/login.html")
    return render(request,"authentication/signup.html",{})

def handlelogin(request):
    return render(request,"authentication/login.html",{})
    
def handlelogout(request):
    return redirect('/auth/login')