from django.contrib import admin

from .models import Meetup

# Register your models here. Registering here is important to show a model in Django Admin

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', )
    prepopulated_fields = {'slug': ('title',)}      ## This is how we auto populate a fiels in django


admin.site.register(Meetup, MeetupAdmin)
