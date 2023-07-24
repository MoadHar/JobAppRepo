from django.contrib import admin

from .models import Person, JobPost, Author


class JobAdmin(admin.ModelAdmin):
    list_display=('title', 'expiry', 'salary', 'author')
    list_filter=('expiry','salary')
    search_fields=('title', 'description')
    search_help_text = "search in title or/and description fields"

    # ------- now detail view
    # fields = (("title", "description"), "salary") //or fieldset bellow, not both
    # exclude = ("expiry")

    fieldsets = (
            ('Basic Information', {
                'fields':('title', 'description')}
             ),
            ('More Information', {
                'classes':('collapse','wide'), # adding builting css stylings
                'fields':(('expiry', 'salary', 'author'), 'slug')}
             ),
    )
# Register your models here.
admin.site.register(JobPost, JobAdmin)
admin.site.register(Author)
admin.site.register(Person)
