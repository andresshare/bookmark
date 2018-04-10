from django.contrib import admin
from .models import Bookmark, Tags

class BookmarkModelAdmin(admin.ModelAdmin):
    list_display=['name','url','datetimeposted','ispublic','get_tags']
    list_filter=['tags']
    search_fields = ['user__name', 'name']

    def get_tags(self, bookmark):
        return ','.join([tag.name for tag in bookmark.tags.all()])




admin.site.register(Bookmark, BookmarkModelAdmin)
admin.site.register(Tags)