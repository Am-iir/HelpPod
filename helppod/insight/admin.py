from django.contrib import admin

# Register your models here.
from .models import Task , HelperSignUp

class TaskAdmin(admin.ModelAdmin):
    list_display=["title" ,"description" ,"service_date","service_time"  ,"pickup_location","drop_location","timestamp" ,"user_name","phone"]
    class Meta:
        model = Task

admin.site.register(Task,TaskAdmin)

class HelperAdmin(admin.ModelAdmin):
    list_display=['first_name']

    class Meta:
        model = HelperSignUp
admin.site.register(HelperSignUp,HelperAdmin)

    