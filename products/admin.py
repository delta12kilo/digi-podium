from django.contrib import admin
from .models import allCourses, CourseFetures

# Register your models here.

@admin.register(allCourses)
class AllCourses(admin.ModelAdmin):
    list_display = (
        'courseId','courseTitle',
        'coursePrice'
    )
    list_filter = ('courseTag','courseSlug')



@admin.register(CourseFetures)
class courseFet(admin.ModelAdmin):
    list_display = ('courseFeatures',)