from django.shortcuts import render, redirect
from .forms import AdminLoginForm, UserLoginForm,  RecruiterLoginForm, UserSignupForm, RecruiterSignupForm, AdminLoginForm, CreateJobForm, ContactUsForm
import re
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
from datetime import date
# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        receipent = request.POST['receipent']
        try:
            newsletter_sub.objects.create(username=username, receipent=receipent)
            error = "no"
        except:
            error = "yes"
        dic = {'error': error}
        return render(request, 'index.html', context=dic)
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
    user = request.user
    current_user = StudentUser.objects.get(user=user)
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        if request.FILES.get('image'):
            image = request.FILES['image']
        else:
            image = current_user.image
        current_user.user.first_name = firstname
        current_user.user.last_name = lastname
        current_user.user.username = username
        current_user.user.email = email
        current_user.mobile = contact
        current_user.image = image
        try:
            current_user.user.save()
            current_user.save()
            mistake = "no"
        except:
            mistake = "yes"
        dic = {'current_user': current_user, 'mistake': mistake}
        return render(request, 'user_home.html', context=dic)
    elif request.method == "GET":
        dic = {'current_user': current_user}
        return render(request, 'user_home.html', context=dic)

def user_signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        # image = request.POST.get('image')
        image = request.FILES['image']
        email = request.POST['email']
        age = request.POST['age']
        contact = request.POST['contact']
        password = request.POST['password']
        # print(image)
        # print(username)
        # print(email)
        # print(password)
        # print(age)
        # print(contact)
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
                recruiter_dictionary = {
                    "form": RecruiterLoginForm,
                    "error": error,
                    "status": user1.status
                }
            except:
                error = "yes"
                recruiter_dictionary = {
                    "form": RecruiterLoginForm,
                    "error": error
                }
        else:
            error = "yes"
            recruiter_dictionary = {
                "form": RecruiterLoginForm,
                "error": error
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
    current_user = request.user
    current_recruiter = Recruiter.objects.get(user=current_user)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        company = request.POST['company']
        email = request.POST['email']
        contact = request.POST['contact']
        if request.FILES.get('image'):
            image = request.FILES['image']
        else:
            image = current_recruiter.image
        current_recruiter.user.first_name = firstname
        current_recruiter.user.last_name = lastname
        current_recruiter.user.username = username
        current_recruiter.user.email = email
        current_recruiter.company = company
        current_recruiter.mobile = contact
        current_recruiter.image = image
        try:
            current_recruiter.user.save()
            current_recruiter.save()
            mistake="no"
        except:
            mistake="yes"
        dic = {'current_recruiter': current_recruiter, "mistake": mistake}
        return render(request, 'recruiter_home.html', context=dic)
    elif request.method == "GET":
        dic = {'current_recruiter': current_recruiter}
        return render(request, 'recruiter_home.html', context=dic)

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
    user_count = StudentUser.objects.all().count()
    recruiter_count = Recruiter.objects.all().count()
    subscriber_count = newsletter_sub.objects.all().count()
    dic = {'user_count': user_count, 'recruiter_count': recruiter_count, 'subscriber_count':subscriber_count}
    return render(request, 'admin_home.html', context=dic)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    dic = {'data': data}
    return render(request, 'view_users.html', dic)

def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    studt = User.objects.get(id=pid)
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

def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    studt = User.objects.get(id=pid)
    studt.delete()
    return redirect('all_recruiters')

def admin_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        try:
            user = User.objects.get(id=request.user.id)
            # password can't be directly compared because it is stored in hash form
            if (user.check_password(current_password)):
                user.set_password(new_password)
                user.save()
                error="no"
            else:
                error="currentwrong"
        except:
            error ="yes"
    dic = {"error":error}
    return render(request, 'admin_password.html', dic) 

def recruiter_password(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        try:
            user = User.objects.get(id=request.user.id)
            # password can't be directly compared because it is stored in hash form
            if (user.check_password(current_password)):
                user.set_password(new_password)
                user.save()
                error="no"
            else:
                error="currentwrong"
        except:
            error ="yes"
    dic = {"error":error}
    return render(request, 'recruiter_password.html', dic)

def user_password(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        try:
            user = User.objects.get(id=request.user.id)
            # password can't be directly compared because it is stored in hash form
            if (user.check_password(current_password)):
                user.set_password(new_password)
                user.save()
                error="no"
            else:
                error="currentwrong"
        except:
            error ="yes"
    dic = {"error":error}
    return render(request, 'user_password.html', dic)

def create_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    if request.method == "POST":
        form = CreateJobForm(request.POST)
        domain = request.POST['domain']
        role = request.POST['role']
        skillset = request.POST['skillset']
        salary = request.POST['salary']
        joining_date = request.POST['joining_date']
        location = request.POST['location']
        logo = request.FILES['logo']
        description = request.POST['description']
        job_creation_date =  date.today()
        print(job_creation_date)
        current_user = request.user
        current_recruiter = Recruiter.objects.get(user=current_user)
        try:
            JobModel.objects.create(recruiter=current_recruiter, domain=domain, role=role, skillset=skillset, salary=salary, joining_date=joining_date, location=location, logo=logo, description=description, job_creation_date=job_creation_date)
            mistake="no"
        except:
            mistake="yes"
        create_job_dic = {
            "form": CreateJobForm,
            "mistake": mistake
        }
        return render(request, 'create_job.html', context=create_job_dic)
    elif request.method=="GET":
        create_job_dic = {
            "form": CreateJobForm
        }
        return render(request, 'create_job.html', context=create_job_dic)

def created_jobs(request):
    if not request.user.is_authenticated:
        return render(request, 'created_jobs.html')
    current_user = request.user
    current_recruiter = Recruiter.objects.get(user=current_user)
    data = JobModel.objects.filter(recruiter=current_recruiter)
    dic = {'data':data}
    return render(request, 'created_jobs.html', context=dic)

def edit_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    current_job_data = JobModel.objects.get(id=pid)
    if request.method == "POST":
        form = CreateJobForm(request.POST)
        domain = request.POST['domain']
        role = request.POST['role']
        skillset = request.POST['skillset']
        salary = request.POST['salary']
        joining_date = request.POST['joining_date']
        location = request.POST['location']
        if request.FILES.get('logo'):
            logo = request.FILES['logo']
        else:
            logo = current_job_data.logo
        if request.FILES.get('job_description_file'):
            job_description_file = request.FILES['job_description_file']
        else:
            job_description_file = current_job_data.job_description_file
        description = request.POST['description']
        current_job_data.domain = domain
        current_job_data.role = role
        current_job_data.skillset = skillset
        current_job_data.salary = salary
        current_job_data.joining_date = joining_date
        current_job_data.location = location
        current_job_data.logo = logo
        current_job_data.description = description
        current_job_data.job_description_file = job_description_file
        try:
            current_job_data.save()
            mistake="no"
        except:
            mistake="yes"
        create_job_dic = {
            "form": CreateJobForm,
            "mistake": mistake,
            "current_job_data": current_job_data
        }
        return render(request, 'edit_job.html', context=create_job_dic)
    elif request.method=="GET":
        create_job_dic = {
            "form": CreateJobForm,
            "current_job_data": current_job_data
        }
        return render(request, 'edit_job.html', context=create_job_dic)

def delete_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    current_job_data = JobModel.objects.get(id=pid)
    current_job_data.delete()
    return redirect('created_jobs')

def latest_jobs(request):
    job_data = JobModel.objects.all().order_by('-joining_date')
    dic = {'data': job_data}
    return render(request, 'latest_jobs.html', context=dic)

def user_latest_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    job_data = JobModel.objects.all().order_by('-joining_date')
    applications = Application.objects.filter(student=student)
    applied_jobs = []
    for i in applications:
        applied_jobs.append(i.job.id)
    dic = {'data': job_data, 'applied_jobs': applied_jobs}
    return render(request, 'user_latest_jobs.html', context=dic)

def job_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    job = JobModel.objects.get(id=pid)
    dic = {'job':job}
    return render(request, 'job_details.html', dic)

def apply(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    job_data = JobModel.objects.get(id=pid)
    if request.method == "POST":
        resume = request.FILES['resume']
        try:
            Application.objects.create(student=student, job=job_data, resume=resume, application_date=date.today())
            mistake="no"
        except:
            mistake="yes"
        dic = {'mistake':mistake}
        return render(request, 'apply.html', context=dic)
    return render(request, 'apply.html')
    
def applications_generated(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    applications_generated = Application.objects.filter(student=student)
    dic = {'applications_generated': applications_generated}
    return render(request, 'applications_generated.html', context=dic)

def applications_received(request):
    if not request.user.is_authenticated:
        return render('recruiter_login')
    applications_received = Application.objects.all()
    data = {'applications_received': applications_received}
    return render(request, 'applications_received.html', context=data)

def contactus(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        try:
            ContactUs.objects.create(name=name, email=email, message=message)
            mistake="no"
        except:
            mistake="yes"
        dic = {
            "form": ContactUsForm,
            "mistake": mistake
        }
        return render(request, 'contactus.html', context=dic)
    dic = {
        "form": ContactUsForm
    }
    return render(request, 'contactus.html',context=dic)

def newsletter_subscribers(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = newsletter_sub.objects.all()
    dic = {'data': data}
    return render(request, 'newsletter_subscribers.html', context=dic)

def delete_sub(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sub = newsletter_sub.objects.get(id=pid)
    sub.delete()
    return redirect('newsletter_subscribers')

import docx2txt
# resume_matcher
def resume_matcher(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    if request.method == "POST":
        resume = request.FILES['resume']
        resume = docx2txt.process(resume)
        job_description = request.FILES['job_description']
        job_description = docx2txt.process(job_description)
        text = [resume, job_description]
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)
        from sklearn.metrics.pairwise import cosine_similarity
        matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        matchPercentage = round(matchPercentage, 2)
        data = {'resume_score':matchPercentage}
        return render(request, 'resume_matcher.html', context=data)
    return render(request, 'resume_matcher.html')

    