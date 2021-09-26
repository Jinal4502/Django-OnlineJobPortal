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
