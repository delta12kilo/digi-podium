from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField, CharField, FloatField
from django.db.models.fields.related import ForeignKey
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils.timezone import now as n
from datetime import date, datetime
# Create your models here.

course = [
    ('mca','M.C.A'),
    ('bca','B.C.A'),
    ('btech','B.Tech'),
    ('bsc','BSc'),
    ('bvoc', 'B.voc')
]

years = [
    ('1','one'),
    ('2','two'),
    ('3','three'),
    ('4','four')
]

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

    def get_absolute_url(self):
        return reverse('npro:nproo',
                        args=[self.courseSlug])


    objects = models.Manager()

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

    objects = models.Manager()


def gen_reg_no():
        
    try:
        curr = date.today()
        yr = curr.year
        last_reg = enroll.objects.all().order_by('e_id').last()
        id_value = int(last_reg.reg_id.split('/')[-1])+1
        
    except Exception as err:
        id_value = 1
        print(err)
        # raise err

    return f'DP/{yr}/{id_value}'

#TODO: change names 
class enroll(models.Model):
        
    e_id = models.AutoField(primary_key=True)
    reg_id = models.CharField( max_length=15,unique=True, default=gen_reg_no)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    imgupl = models.ImageField(upload_to='enroll',default="None")
    email = models.EmailField(default="None")
    
    phoneNumber = models.CharField(max_length=15,default='1234')
    WphoneNumber = models.CharField(max_length=15,default='1234')

    collegess = models.CharField(max_length=100, default='CollegeName')

    courses = models.CharField(max_length=6, default="None")
    year = models.CharField(max_length=1, default="None")
    created = models.DateTimeField(auto_now_add=True)
    program = models.CharField(max_length=100,default="None")    
    price = models.CharField(max_length=100,default="None")

    def __str__(self):
        return self.reg_id


    objects = models.Manager()

class Installment(models.Model) :
    enr_id = models.AutoField(primary_key=True)
    enrollment_no = models.OneToOneField(enroll, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_no = models.CharField(max_length=100)
    submit = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.transaction_no


    