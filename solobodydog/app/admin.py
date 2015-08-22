from django.contrib import admin

# Register your models here.
from .models import User, LoginHistory, UserProfile

admin.site.register(User)
admin.site.register(LoginHistory)
admin.site.register(UserProfile)