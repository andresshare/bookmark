from __future__ import unicode_literals
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404
from bookmark.models import Bookmark
from django.contrib.auth.models import User

def all_bookmarks(request):
    bookmarks = Bookmark.objects.filter(ispublic=True)
    return render(request, 'bookmark/all_bookmarks.html',{'bookmarks':bookmarks})

#def  bookmark_detail(request, bookmark_id):
   # if bookmark_id == '0':
    #    return HttpResponseNotFound("Not Found")
   # else:
    #    return HttpResponse("bookmark id=%s" % bookmark_id)

def  bookmark_by_user(request, username):
    user = get_object_or_404(User, username=username)
    bookmarks = Bookmark.objects.filter(user=user)
    return render(request,'bookmark/detail.html', {'bookmarks':bookmarks,'user':'user'})