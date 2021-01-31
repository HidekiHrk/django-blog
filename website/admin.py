from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.site_header = 'CMS HidekiHrk'


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "sub_title")
    
    def get_form(self, request, obj, **kwargs):
        self.exclude = ('slug',)
        return super(PostAdmin, self).get_form(request, obj=obj, **kwargs)

admin.site.register(Post, PostAdmin)
