from bookmark import views
from django.conf.urls import  url


urlpatterns = [
    url(r'^all/$', view=views.AllBookmarksView.as_view(), name='all-bookmarks'),
    url(r'^detail-page/(?P<username>[\w]+)/$',view=views.BookmarkByUser.as_view(),name='detail-route'),
    url(r'^create/$', view=views.createbookmarkview.as_view(), name='create-bookmark')


]