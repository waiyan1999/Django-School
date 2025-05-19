from django.shortcuts import render,redirect,HttpResponse
from myapp1.models import Teacher,Course
from myapp1.form import ModelForm

from django.contrib.auth.models import User  # aut-table
from django.contrib.auth import authenticate,login,logout  # authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')

def course_details(request):
    return render(request,'course-detail.html')

def courses(request):
    course_data = Course.objects.all()
    context = {'course_data':course_data}
    return render(request,'courses.html',context)

@login_required(login_url='login')
def events(request):
    return render(request,'events.html')

def pricing(request):
    return render(request,'pricing.html')

def starter_page(request):
    return render(request,'starter-page.html')

def trainers(request):
    return render(request,'trainers.html')

def base(request):
    return render(request,'base.html')

def createCourse(request):
    fm = ModelForm() 
    context = {'fm':fm}
    return render(request,'createcourse.html',context)

def saveCourse(request):
    if request.method == 'POST':
        fm = ModelForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
        else:
            print( "Error Occur")
            
    return redirect('courses')

def saveCourse1(request):
    if request.method == 'POST':
        fm = ModelForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            print('Successfully Saved.')
        else:
            print( "Error Occur")
            
    return redirect('courses')
            
            
def courseUpdate(request,id):
    update_course_data = Course.objects.filter(id=id)
    context = {'update_coures_data':update_course_data}
    return render(request,'updatecourse.html',context)

def courseUpdateSave(request,id):
    d = Course.objects.get(id=id)
    
    # context = {'save_update_course_data':save_update_course_data}
    # return redirect('courses')
    
    form = ModelForm(request.FILES,request.POST,instance = d)
    
    if form.is_valid():
        form.save()
        print('Updated Data successfully save')
        
    else:
        print("Updated Data Cannot Save. ! Error Occur")
        print(form.errors)
        
    return redirect('courses')


def courseDetail(request,id):
    course_details = Course.objects.filter(id=id)
    context = {'course_details':course_details}
    return render(request,'coursedetails.html',context)

def deleteCourse(request,id):
    course_delete = Course.objects.filter(id=id)
    #course_name = course_delete.c_name
    course_delete.delete()
   # print(f"Course {course_name} Deleted")
    return redirect('courses')


def updatecourse1(request,id):
    obj = Course.objects.filter(id=id)
    
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_note = request.POST.get('course_note')
        course_fee = request.POST.get('course_fee')
        course_photo = request.FILES.get('course_photo')
        
        obj.update(c_name = course_name , c_note = course_note , fee = course_fee, c_photo = course_photo)
        return redirect('courses')
    
    context = {'update':obj}
    
    return render(request,'updatecourse1.html',context)

# =================== Day 14  Djanog 9 ==========================

def loginView(request):
    
    if request.method == 'POST':
        username = request.POST.get('l_name')
        password = request.POST.get('l_password')
        
        
        # if username == 'admin' and password == 'admin':
        #     print('Login in Successfully')
        #     return redirect('index')
        # else:
        #     return render(request,'login.html')
   
        
        usr_auth = authenticate(username = username,password = password)
        if usr_auth:
            print ('success')
            # return HttpResponse('Success')
            login(request,usr_auth)
            return redirect('index')
        
        else:
            print ('fail')
            # return HttpResponse('Error')
            return redirect('login')
        
    else:
        return render(request,'login.html')
    


def logoutView(request):
    logout(request)
    return redirect('login')  
        



