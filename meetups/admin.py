from django.contrib import admin

from .models import Meetup, Location, Particiant

# Register your models here. Registering here is important to show a model in Django Admin

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title',)}      ## This is how we auto populate a fiels in django


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Particiant)
