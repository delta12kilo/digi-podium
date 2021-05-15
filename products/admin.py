from django.contrib import admin
from .models import It_allCourses,sophomore, enroll, Installment

# Register your models here.

@admin.register(It_allCourses)
class AllCourses(admin.ModelAdmin):
    list_display = (
        'courseId','courseTitle',
        'coursePrice'
    )
    list_filter = ('courseTag','courseSlug')


@admin.register(sophomore)
class Sophomore(admin.ModelAdmin):
    list_display = (
        's_courseID','s_courseheading',
        's_course_slug', 's_course_price'
    )

    

@admin.register(enroll)
class Enroll(admin.ModelAdmin):
    list_display = ('e_id','firstName',
                    'lastName','courses','email', 
                    'program', 'created'
                )

    list_filter = ('program','courses')

@admin.register(Installment)
class installment(admin.ModelAdmin):
    list_display = ('enr_id','enrollment_no',
                    'amount')

    list_filter = ('enrollment_no',)