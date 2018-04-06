from bookmark import views
from django.conf.urls import  url


urlpatterns = [
    url(r'^all/$', view=views.AllBookmarksView.as_view()),
    url(r'^detail-page/(?P<username>[\w]+)/$',view=views.BookmarkByUser.as_view(),name='detail-route')


]