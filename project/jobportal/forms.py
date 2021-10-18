from django import forms

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Minimun 6-digits'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email-address'}))

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Minimun 6-digits'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email-address'}))

class RecruiterLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Minimun 6-digits'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email-address'}))

class UserSignupForm(forms.Form):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    image = forms.ImageField(required=False, label='Profile Photo', widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'File format must be .jpg, .jpeg or .png'})) 
    password = forms.CharField(max_length=30, min_length=6 , widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Minimun 6-digits'}))
    password_verification = forms.CharField(label = "", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Re-Enter Password'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email-address'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age should be 18 or above'}))
    contact = forms.CharField(label='Contact Number', max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your mobile number: '}))
    

class RecruiterSignupForm(forms.Form):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company for which you will recruit?'}))
    image = forms.ImageField(required=False, label='Profile Photo', widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'File format must be .jpg, .jpeg or .png'})) 
    password = forms.CharField(max_length=30, min_length=6 , widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Minimun 6-digits'}))
    password_verification = forms.CharField(label = "", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Re-Enter Password'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email-address'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age should be 18 or above'}))
    contact = forms.CharField(label='Contact Number', max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your mobile number: '}))

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Minimun 6-digits'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter Email-address'}))

class CreateJobForm(forms.Form):
    domain = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the domain for the job'}))
    role = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the role of job for which you intend to recruit'}))
    skillset = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mention the skills you are looking for in the candidate'}))
    salary = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Monthy Income'}))
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'yyyy-mm-dd'}))
    location = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the working location'}))
    logo = forms.ImageField(required=False, label='Company Logo', widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'File format must be .jpg, .jpeg or .png'})) 
    description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Any further details you wish to mention'}))
    job_description_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your full-name'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email-address'}))
    message = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Message'}))