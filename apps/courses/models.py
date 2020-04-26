from django.db import models 
from ..login_reg.models import *
import re 
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 
 


class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters"
        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            errors['desc'] = "Description is optional, but must be at least 10 characters if used"

        return errors

    def duplicate_validator(self, postData):
        duplicate = {}
        if len(Course.objects.filter(name=postData['name'])):
            duplicate['duplicate'] = "Course already exists"

        return duplicate




class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default="Description...")
    date_added = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users_in_course = models.ManyToManyField("login_reg.User", related_name="courses_enrolled_in", verbose_name=("users_who_enrolled_in_this_course"))
    objects = CourseManager()



