from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.




class It_allCourses(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseImage = models.ImageField()
    courseTitle = models.CharField(max_length=250)
    courseSummary = models.CharField(max_length=300)
    courseDiscrp = models.TextField()
    courseSlug = models.SlugField(unique=True,max_length=100)
    courseTag = TaggableManager()
    coursePrice = models.IntegerField()
    coursePublish = models.DateTimeField(auto_now_add=True)
    courseVersion = models.CharField(max_length=20, default='0.0')
    s_courseFeature = models.CharField(max_length=200)
    courseFeature1 = models.CharField(max_length=200, default='feature')
    courseFeature2 = models.CharField(max_length=200,default='feature')
    courseFeature3 = models.CharField(max_length=200,default='feature')
    courseFeature4 = models.CharField(max_length=200,default='feature')
    courseFeature5 = models.CharField(max_length=200,default='feature')
    courseImage_sml_1 = models.ImageField(default='def.jpg')
    courseImage_sml_2 = models.ImageField(default='def2.jpg')

    def __str__(self):
        return self.courseTitle


class sophomore(models.Model):
    s_courseID = models.AutoField(primary_key=True)
    s_courseheading = models.CharField(max_length=250)
    s_course_desc = models.TextField()
    s_course_slug = models.SlugField(unique=True,max_length=100)
    s_course_tag = TaggableManager()
    s_course_price = models.IntegerField()
    s_courseFeature = models.CharField(max_length=200, default='feature')
    s_courseFeature1 = models.CharField(max_length=200, default='feature')
    s_courseFeature2 = models.CharField(max_length=200, default='feature')
    s_courseFeature3 = models.CharField(max_length=200, default='feature')
    s_courseFeature4 = models.CharField(max_length=200, default='feature')
    s_courseFeature5 = models.CharField(max_length=200, default='feature')
    s_course_img_big = models.ImageField()
    s_course_img_sml1 = models.ImageField()
    s_course_img_sml2 = models.ImageField()
    s_course_img_sml3 = models.ImageField()


    def _str__(self):

        return self.s_courseheading
