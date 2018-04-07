from django.contrib import admin

# Register your models here.


from .models import Bookmark

#class BookmarkModelAdmin(admin.ModelAdmin):
 #   list_display=['name','url','datetimeposted','ispublic','get_tags']
  #  list_filter=['tags']
    #search_fields = ['user__name','name']

   # def get_tags(self,bookmark):
    #    return ','.join([tag.name for tag in bookmark.tags.all()])




admin.site.register(Bookmark)

