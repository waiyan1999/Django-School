from django.urls import path
from myapp1.views import *




urlpatterns = [
   
    path('', index, name = 'index'),
    path('about/',about , name = 'about'),
    path('contact/',contact, name = 'conatce'),
    path('coursedetails/',course_details,name = 'coursedetails'),
    path('courses/', courses , name = 'courses'),
    path('events/', events , name = 'events'),
    path('pricing/',pricing, name = 'pricing'),
    path('starterpage/',starter_page, name = 'starterpage'),
    path('trainers/',trainers,name = 'trainers'),
    path('createcourse/',createCourse, name = 'createcourse'),
    path('savecourse/',saveCourse, name = 'savecourse'),
    path('courseupdate/<int:id>/',courseUpdate, name = 'courseupdate'),
    path('courseupdatesave/<int:id>/',courseUpdateSave , name = 'courseupdatesave'),
    path('coursedetails/<int:id>/',courseDetail, name = 'coursedetails'),
    path('deletecourse/<int:id>/',deleteCourse, name = 'deletecourse'),
    path('updatecourse1/<int:id>/',updatecourse1, name = 'updatecourse1'),
    path('login/',loginView, name = 'login'),
    path('logout/',logoutView, name = 'logout'),
    
    
]