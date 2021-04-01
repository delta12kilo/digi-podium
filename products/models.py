from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class CourseFetures(models.Model):
    courseFeatures = models.CharField(max_length=100)


    def __str__(self):
        return self.courseFeatures


class allCourses(models.Model):
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
    courseFeature = models.ForeignKey(CourseFetures,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.courseTitle
