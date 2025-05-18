from django.db import models

# Create your models here.

class Course(models.Model):
     c_photo = models.ImageField(upload_to='course_photo')
     c_name =  models.CharField()
     fee = models.PositiveIntegerField()
     c_note = models.TextField()
     c_time = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return self.c_name
     
     
class Teacher(models.Model):
    
    t_photo = models.ImageField(upload_to='teacher_photo')
    t_name = models.CharField()
    course = models.CharField()
    t_note = models.TextField()
    t_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.t_name
    