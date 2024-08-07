from django.contrib import admin
from .models import Profile, Bookmark

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    list_display = ("user", "phoneNo", "address",)
    list_filter = ("user",)

admin.site.register(Profile, ProfileAdmin)

class BookmarkAdmin(admin.ModelAdmin):

    list_display = ("user", "created_at",)
    list_filter = ("user",)

admin.site.register(Bookmark, BookmarkAdmin)