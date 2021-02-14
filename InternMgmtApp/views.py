from django.shortcuts import render, redirect
from .models import application_details
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms


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
    if request.method == 'POST':
        username = request.POST['username']
        pas = request.POST['password']
    
        user = auth.authenticate(username=username,password=pas)

        if user is not None:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/displayJobPosting')

        else:
            error_msg = 'Invalid credentials'
            return render(request,'login.html',{'error':error_msg})
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
        pas1 = request.POST['password1']
        pas2 = request.POST['password2']

        error_msg = None

        if pas1 == pas2:
            if User.objects.filter(username=user).exists():
                error_msg = 'User exists!'
                return render(request,'register.html',{'error':error_msg})

            elif User.objects.filter(email=email).exists():
                error_msg = 'Email exists!'
                return render(request,'register.html',{'error':error_msg})
            else:
                user = User.objects.create_user(username=user,first_name=fname,last_name=lname,email=email,password=pas1)
                user.save()
                return redirect('/')
    else:
        return render(request,'register.html')

def displayJobPosting(request):
    return render(request,'jobPosting.html')


def displaySubPost(request):
    if(request.POST.get('web')):
        return render(request,'subPosting.html',
        {'stream1':'HTML-5', 'stream2':'PHP', 'stream3':'JavaScript',
        'img1':'images/html.jpg', 'img2':'images/php.jpg', 'img3':'images/javascript.jpg',
        'msg1':'Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser.',
        'msg2':'PHP is a general-purpose scripting language especially suited to web development.',
        'msg3':'JavaScript, often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.'
        })
    
    if(request.POST.get('android')):
        return render(request,'subPosting.html',
        {'stream1':'JAVA-Android', 'stream2':'Kotlin-Android',
        'img1':'images/java.jpg', 'img2':'images/android.jpg',
        'msg1':'Java is the technology of choice for building applications using managed code that can execute on mobile devices.',
        'msg2':'Kotlin is an open-source, statically-typed language that supports both object-oriented and functional programming.',
        })

    if(request.POST.get('network')):
        return render(request,'subPosting.html',
        {'stream1':'CPP-Networking', 'stream2':'JAVA-Networking',
        'img1':'images/networking.jpg', 'img2':'images/java.jpg',
        'msg1':'C++ is a cross-platform language used to create high-performance applications. C++ was developed by Bjarne Stroustrup.',
        'msg2':'Java is the technology of choice for building applications using managed code that can execute on mobile devices.',
        })

def apply(request):
    if(request.POST.get('HTML-5')):
        return render(request,'apply.html',{'head':'Web-Development(HTML-5)'})
    
    if(request.POST.get('PHP')):
        return render(request,'apply.html',{'head':'Web-Development(PHP)'})
    
    if(request.POST.get('JavaScript')):
        return render(request,'apply.html',{'head':'Web-Development(JavaScript)'})

def addApplicantDetails(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        university = request.POST['university']
        phone = request.POST['phone']
        applied_in = request.POST['field']
        resume = request.FILES['docfile']

        if application_details.objects.filter(email=email).exists():
            messages.error(request,'Email exists')
            return render(request, 'apply.html')

        elif application_details.objects.filter(phone=phone).exists():
            messages.error(request,'Contact exists')
            return render(request, 'apply.html')

        else:
            applicant = application_details()
            applicant.fname = fname
            applicant.lname = lname
            applicant.email = email
            applicant.applied_in = applied_in
            applicant.phone = phone
            applicant.university = university
            applicant.resume = resume

            applicant.save()
            messages.success(request,'Application Successfull')
            return render(request, 'home.html')

    return render(request, 'home.html')

def retrieveData(request):
    data = application_details.objects.get(fname='Pranav')
    print(data.lname)
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')