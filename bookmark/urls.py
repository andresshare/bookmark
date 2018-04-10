from bookmark import views
from django.conf.urls import  url


urlpatterns = [
    url(r'^all/$', view=views.AllBookmarksView.as_view(), name='all-bookmarks'),
    url(r'^detail-page/(?P<username>[\w]+)/$',view=views.BookmarkByUser.as_view(),name='detail-route'),
    url(r'^create/$', view=views.CreateBookmarkView.as_view(), name='create-bookmark'),
    url(r'^update/(?P<pk>[0-9]+)/$', view=views.UpdateBookmarkView.as_view(), name='update-bookmark')


]