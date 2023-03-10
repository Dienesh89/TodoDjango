from django.shortcuts import render, HttpResponse, redirect
from todo.models import signup, Task
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
import re

# function for validation of password
def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True  

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        todos = Task.objects.filter(Taskuser = request.user)
        return render(request, "index.html",context = {"todos":todos})
    else:
        return redirect("/signup")

def signUp(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        return render(request,"signup.html")

def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        return render(request,"login.html")

def handleSignup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]


        # Adding some basic checjs to the form

        # username should be Alpha Numeric
        if (username.isalnum() == True):
            Alnum = True
        else:
            messages.error(request, "Username should be Alpha Numeric ")
            return redirect("/signup")

        # length of username should be between 8 and 12
        if ((len(username)>=8) and (len(username)<=12)):
            TrueUserNameLen = True
        else:
            messages.error(request, "Length of the username must be between 8 and 12 ")
            return redirect("/signup")

        # validating the password
        if (validate_password(password)):
            correctPassword = True
        else:
            messages.error(request,"Password should contain at least one UpperCase,LowerCase,number and symbol. ")
            return redirect("/signup")

        # checking the password and cpassword is equal
        if (password == cpassword):
            equalPassword = True
        else:
            messages.error(request,"Passwords are not equal. ")
            return redirect("/signup")

        # checking if username already exists or not
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
            return redirect("/signup")
        else:
            UniqueUsername = True


        # If user filled the forn correctly.
        if (Alnum == True and 
            TrueUserNameLen == True and
            correctPassword == True and
            equalPassword == True and
            UniqueUsername == True ):

            Signup = signup(username = username,password = password)
            Signup.save()
            # creating the user
            myuser = User.objects.create_user(username=username,password=password)
            myuser.email = "Not set"
            myuser.first_name = username
            myuser.last_name = "Not set"
            # saving the user
            myuser.save()

            messages.success(request,"Your account has been created successfully ")
            return redirect("/login")
        
    else:
        return HttpResponse("404-Not found")

# login and logout
def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request,user)
            messages.success(request, "You are Succesfully Logged In.")
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("/login")
    else:
        return HttpResponse("404 - Not Found")

def handleLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You are successfully Loggedout.")
        return redirect("/login")
    else:
        messages.error(request,"You are not LoggedIn to Logout")
        return redirect("/login")

def addTodo(request):
    if request.method == "POST":
        task = request.POST["task"]
        user = request.user
        task = Task(task=task,Taskuser=user)
        task.save()
        return redirect("/")
    else:
        return HttpResponse("404 - Not Found")
def deleteTodo(request,id):
    if request.method == "POST":
        Task.objects.get(pk=id).delete()
        return redirect("/")
    else:
        return HttpResponse("404 - Not Found")


