from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from django.db.models import Count
 
 
# Create your views here. 
def index(request): 
    all_courses = Course.objects.all()
    context = {
        "all_courses" : all_courses,
    }
    return render(request, 'courses/index.html', context) 


def newCourse(request):

    errors = Course.objects.validator(request.POST)

    duplicate = Course.objects.duplicate_validator(request.POST)

    if len(duplicate) > 0:
        messages.error(request, duplicate)
        return redirect('/courses/')

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request,v)
        return redirect('/')
    else:
        messages.success(request, "Course added!")
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/courses/')


def destroyCourse(request, id):
    delCourse = Course.objects.get(id=id)
    context = {
        "course" : delCourse,
    }
    return render(request, "courses/destroy.html", context)

def userCourses(request):

    all_courses = Course.objects.all()
    all_users = User.objects.all()
    courseNumUsers = Course.objects.annotate(num_users=Count('users_in_course'))
    context = {
        "all_courses" : all_courses,
        "all_users" : all_users,
    }


    return render(request, "courses/user_courses.html", context)


def addUserToCourse(request):
    thisUser = User.objects.get(id=request.session['cur_user'])
    thisClass = Course.objects.get(id=request.POST['course'])

    thisClass.users_in_course.add(thisUser)
    thisClass.save()

    return redirect('/courses/userCourses/')

def deleteCourse(request, id):
    delCourse = Course.objects.get(id=id)
    delCourse.delete()
    return redirect('/courses/')


