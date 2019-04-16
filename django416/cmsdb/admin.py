from django.contrib import admin

# Register your models here.
from cmsdb import models

admin.site.register(models.Userinfo)
admin.site.register(models.Usertype)