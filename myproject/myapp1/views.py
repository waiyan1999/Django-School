from django.shortcuts import render,redirect
from myapp1.models import Teacher,Course
from myapp1.form import ModelForm

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
        
        



    