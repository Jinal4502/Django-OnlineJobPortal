from django.shortcuts import render, redirect
from .forms import AdminLoginForm, UserLoginForm,  RecruiterLoginForm, UserSignupForm, RecruiterSignupForm, AdminLoginForm
import re
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User = authenticate(username = username, password = password, email = email)
        if User:
            try:
                user1 = StudentUser.objects.get(user=User)
                if user1.user_type == "Student User":
                    login(request, User)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
        user_dictionary = {
            "form": UserLoginForm,
            "error": error
        }
        return render(request, 'user_login.html', context=user_dictionary)

    elif request.method == "GET":
        form = UserLoginForm
        user_dictionary = {
            "form": form
        }
        return render(request, 'user_login.html', context=user_dictionary)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')

def user_signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        # image = request.POST.get('image')
        image = request.FILES['image']
        print(image)
        print(username)
        email = request.POST['email']
        age = request.POST['age']
        contact = request.POST['contact']
        password = request.POST['password']
        password = str(password)
        password_verification = request.POST['password_verification']
        password_verification = str(password_verification)
        if (password != password_verification):
            user_signup_dic = {
                "form": UserSignupForm,
                "error": "Password doesn't match!"
            }
            return render(request, 'user_signup.html', context = user_signup_dic)
        try:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            StudentUser.objects.create(user=user, mobile=contact, image=image, user_type="Student User")
            mistake="no"
        except:
            mistake="yes"
        user_signup_dic = {
            "form": UserSignupForm,
            "mistake": mistake
        }
        return render(request, 'user_signup.html', context=user_signup_dic)

    elif request.method == "GET":
        form = UserSignupForm
        user_signup_dic = {
            "form": UserSignupForm
        }
        return render(request, 'user_signup.html', context=user_signup_dic)


def log_out(request):
    logout(request)
    return redirect('index')

def recruiter_signup(request):
    if request.method == "POST":
        form = RecruiterSignupForm(request.POST)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        company = request.POST['company']
        # image = request.POST.get('image')
        image = request.FILES['image']
        email = request.POST['email']
        age = request.POST['age']
        contact = request.POST['contact']
        password = request.POST['password']
        password = str(password)
        password_verification = request.POST['password_verification']
        password_verification = str(password_verification)
        if (password != password_verification):
            recruiter_signup_dic = {
                "form": RecruiterSignupForm,
                "error": "Password doesn't match!"
            }
            return render(request, 'recruiter_signup.html', context = recruiter_signup_dic)
        try:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            Recruiter.objects.create(user=user, mobile=contact, image=image, company=company, user_type="Recruiter", status="pending")
            mistake="no"
        except:
            mistake="yes"
        recruiter_signup_dic = {
            "form": RecruiterSignupForm,
            "mistake": mistake
        }
        return render(request, 'recruiter_signup.html', context=recruiter_signup_dic)
    
    elif request.method == "GET":
        form = RecruiterSignupForm
        recruiter_signup_dic = {
            "form": RecruiterSignupForm
        }
        return render(request, 'recruiter_signup.html', context=recruiter_signup_dic)

def recruiter_login(request):
    if request.method == "POST":
        form = RecruiterLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User = authenticate(username = username, password = password, email = email)
        if User:
            try:
                user1 = Recruiter.objects.get(user=User)
                if user1.user_type == 'Recruiter' and user1.status == "accepted":
                    login(request, User)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
        recruiter_dictionary = {
            "form": RecruiterLoginForm,
            "error": error,
            "status": user1.status
        }
        return render(request, 'recruiter_login.html', context=recruiter_dictionary)

    elif request.method == "GET":
        form = RecruiterLoginForm
        recruiter_dictionary = {
            "form": form
        }
        return render(request, 'recruiter_login.html', context=recruiter_dictionary)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, 'recruiter_home.html')

def admin_login(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
        admin_dictionary = {
            "form": AdminLoginForm,
            "error": error
        }
        return render(request, 'admin_login.html', admin_dictionary)

    elif request.method == "GET":
        form = AdminLoginForm
        admin_dictionary = {
            "form": form
        }
        return render(request, 'admin_login.html', admin_dictionary)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    dic = {'data': data}
    return render(request, 'view_users.html', dic)

def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    studt = StudentUser.objects.get(id=pid)
    studt.delete()
    return redirect('view_users')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    dic = {'data': data}
    return render(request, 'recruiter_pending.html', dic)

def recruiter_accept(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin login')
    recrt = Recruiter.objects.get(id=pid)
    recrt.status = "accepted"
    recrt.save()
    return redirect('recruiter_pending')


def recruiter_reject(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin login')
    recrt = Recruiter.objects.get(id=pid)
    recrt.status = "rejected"
    recrt.save()
    return redirect('recruiter_pending')


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin login')
    data = Recruiter.objects.filter(status = "accepted")
    dic = {'data': data}
    return render(request, 'recruiter_accepted.html', dic)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin login')
    data = Recruiter.objects.filter(status = "rejected")
    dic = {'data': data}
    return render(request, 'recruiter_rejected.html', dic)

def all_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin login')
    data = Recruiter.objects.all()
    dic = {'data': data}
    return render(request, 'all_recruiters.html', dic)

def accept_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin login')
    recrt = Recruiter.objects.get(id=pid)
    recrt.status = "accepted"
    recrt.save()
    return redirect('all_recruiters')


def reject_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin login')
    recrt = Recruiter.objects.get(id=pid)
    recrt.status = "rejected"
    recrt.save()
    return redirect('all_recruiters')
#remove this line afterwards
