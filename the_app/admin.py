from django.contrib import admin

from .models import Person, JobPost


class JobAdmin(admin.ModelAdmin):
    list_display=('title', 'expiry', 'salary')

# Register your models here.
admin.site.register(JobPost, JobAdmin)
admin.site.register(Person)
