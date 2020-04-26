from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.index), 
    path('add/', views.newCourse), 
    path('userCourses/', views.userCourses), 
    path('addUserToCourse/', views.addUserToCourse), 
    path('destroy/<int:id>/', views.destroyCourse), 
    path('destroy/<int:id>/delete/', views.deleteCourse), 

] 
 
 
