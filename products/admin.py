from django.contrib import admin
from .models import It_allCourses,sophomore

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