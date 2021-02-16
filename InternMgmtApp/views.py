from django.shortcuts import render, redirect
#from .models import application_details
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms
from .models import CustomUser, ApplicationDetails
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html',{'link':'http://127.0.0.1:8000/register'})

#For Login
def loginView(request):
    return render(request,'login.html')

def subPost1(request):
    return render(request,'subPosting.html')    

def subPost2(request):
    return render(request,'subPosting2.html')    

def subPost3(request):
    return render(request,'subPosting3.html')    

def subPost4(request):
    return render(request,'subPosting4.html')    

def subPost5(request):
    return render(request,'subPosting5.html')    

def subPost6(request):
    return render(request,'subPosting6.html')    

def validateLogin(request):
    print('hey')
    if request.method == 'POST':
        username = request.POST['username']
        pas = request.POST['password']
    
        user = auth.authenticate(username=username,password=pas)

        if user is not None:
            auth.login(request, user)
            return redirect('displayJobPosting')

        else:
            messages.error(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'result.html')

def register(request):
    return render(request,'register.html')

def register1(request):
    if request.method == 'POST':
        user = request.POST['user']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        university = request.POST['university']
        phone = request.POST['phone']
        pas1 = request.POST['password1']
        pas2 = request.POST['password2']

        try:
            validate_password(pas1)
        except ValidationError as e:
            return render(request, 'register.html', {'error': e})

        if pas1 == pas2:
            if CustomUser.objects.filter(username=user).exists():
                messages.error(request,'User already exists')
                return render(request,'register.html')

            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return render(request,'register.html')
            else:
                user = CustomUser.objects.create_user(username=user,first_name=fname,last_name=lname,email=email,password=pas1,university=university,phone=phone)
                user.save()
                messages.success(request,'Registration Successful')
                return redirect('loginView')
    else:
        return render(request,'register.html')

@login_required(login_url="loginView")
def displayJobPosting(request):
    return render(request,'jobPosting.html')

@login_required(login_url="loginView")
def displaySubPost(request):
    data = {}
    if(request.POST.get('web')):
        data = {'stream1':'HTML-5', 'stream2':'PHP', 'stream3':'JavaScript',
        'img1':'images/html.jpg', 'img2':'images/php.jpg', 'img3':'images/javascript.jpg',
        'msg1':'Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.',
        'msg2':'PHP is a general-purpose scripting language especially suited to web development.',
        'msg3':'JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.'
        }
    
    if(request.POST.get('android')):
        data = {'stream1':'JAVA-Android', 'stream2':'Kotlin-Android',
        'img1':'images/java.jpg', 'img2':'images/android.jpg',
        'msg1':'Java is the technology of choice for building applications using managed code that can execute on mobile devices.',
        'msg2':'Kotlin is an open-source, statically-typed language that supports both object-oriented and functional programming.',
        }

    if(request.POST.get('network')):
        data = {'stream1':'CPP-Networking', 'stream2':'JAVA-Networking',
        'img1':'images/networking.jpg', 'img2':'images/java.jpg',
        'msg1':'C++ is a cross-platform language used to create high-performance applications. C++ was developed by Bjarne Stroustrup.',
        'msg2':'Java is the technology of choice for building applications using managed code that can execute on mobile devices.',
        }

    return render(request,'subPosting.html',data)
        



@login_required(login_url="loginView")
def apply(request):
    data = {}
    if(request.POST.get('HTML-5')):
        data = {"field": "Web-Developement(HTML-5)","user":request.user}
    if(request.POST.get('PHP')):
        data = {'field':'Web-Development(PHP)',"user":request.user}
    if(request.POST.get('JavaScript')):
        data = {'field':'Web-Development(JavaScript)',"user":request.user}
    
    return render(request, 'apply.html', data)

@login_required(login_url="loginView")
def addApplicantDetails(request):
    if request.method == 'POST':
        applied_in = request.POST['field']
        resume = request.FILES['docfile']

        if ApplicationDetails.objects.filter(user=request.user, applied_in=applied_in).exists():
            messages.error(request,'Already applied')
            return render(request, 'apply.html')

        else:
            applicant = ApplicationDetails()
            applicant.user = request.user
            applicant.applied_in = request.user
            applicant.applied_in = applied_in
            applicant.resume = resume

            applicant.save()
            messages.success(request,'Application Registered Successful')
            return render(request, 'home.html')

    return render(request, 'home.html')

def retrieveData(request):
    #data = application_details.objects.get(fname='Pranav')
    #print(data.lname)
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')