from django.contrib import admin
from myapp.models import Resume

# Register your models here.

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob','gender', 'locality', 'city','pin', 'provinces','mobile', 'job_city',
                    'profile_image','my_file']
