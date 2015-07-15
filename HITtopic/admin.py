from django.contrib import admin

# Register your models here.

from HITtopic.models import *

admin.site.register(MyUser)
admin.site.register(Topic)
