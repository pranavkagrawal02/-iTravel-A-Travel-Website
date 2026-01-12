from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        # Process registration data here
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            if User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('/')
                else:
                    messages.info(request,'Email already used')
            else:
                messages.info(request,'Username already used')
        else:
            messages.info(request,'Passwords and Confirmation mismatch')



    return render(request,'register.html')  


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')

    return render(request,'login.html')