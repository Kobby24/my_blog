from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(AuthUser)
# admin.site.register(BlogPost)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)

admin.site.register(Leaders)
admin.site.register(Like)
admin.site.register(AboutPageBackground)