from django.contrib import admin
from .models import Post,Comment,User,Block


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","content","created_on","updated_on",)
    list_filter = ("title","content","created_on","updated_on",)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.author):
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.author=request.user
        super().save_model(request,obj,form,change)

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_content","created","edited",]
    def has_change_permission(self, request, obj=None):
        if obj is not None and (request.user==obj.comment_author):
            return True
        return False
admin.site.register(Comment,CommentAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(User,UserAdmin)

class BlockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Block,BlockAdmin)