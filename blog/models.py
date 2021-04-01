from django.db import models
from django.utils import timezone
# Create your models here.

courses = [
    ('py','Python'),
    ('jv','Java'),
    ('php','PHP'),
    ('js','Java Script')
]


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    contact = models.SmallIntegerField(default=123)
    batch = models.CharField(max_length=50,default='Monday')

    courses = models.CharField(max_length=30, choices=courses, default=None)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    objects = models.Manager()


class About(models.Model):
    profile_pic = models.ImageField()
    name = models.CharField(max_length=50)
    exprt = models.CharField(max_length=60,default="Exprt")
    certi = models.CharField(max_length=100)
    
    yrs_exp = models.IntegerField()

    def __str__ (self):
        return self.name
        
    objects = models.Manager()


class course(models.Model):
    prog_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=30)
    no_of_course = models.CharField(max_length=10,default='One')
    name_of_pro = models.CharField(max_length=50,default='Core Java and Advanced Java with Frameworks')
    certi = models.CharField(max_length=40)
    program_dis = models.TextField()
    project_cat = models.TextField()
    primary_image = models.ImageField(upload_to='')
    small_img1 = models.ImageField()
    small_img2 = models.ImageField()


    def __str__ (self):

        return self.program_name

    objects = models.Manager()

