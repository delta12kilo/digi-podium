from django.contrib import admin
from .models import About, course, Payment
# Register your models here.

# admin.site.register(Post)
@admin.register(Payment)
class payments(admin.ModelAdmin):
    list_display = ('pay_id','name','last_name','email','date_time','batch')
    

@admin.register(About)
class about(admin.ModelAdmin):
    list_display = ('name','yrs_exp','exprt')
    list_filter = ('name','certi','exprt')

@admin.register(course)
class Course(admin.ModelAdmin):
    list_display = ('prog_id', 
                    'program_name',
                    'no_of_course',
                )
    list_filter = ( 'program_name',
                    'name_of_pro'
                )