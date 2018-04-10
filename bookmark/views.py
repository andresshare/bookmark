
from __future__ import unicode_literals

from bookmark.forms import CreateBookmarkForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404, HttpResponseRedirect,HttpResponseForbidden
from bookmark.models import Bookmark
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.utils.decorators import method_decorator



class AllBookmarksView(ListView):
    model = Bookmark
    template_name ='bookmark/all_bookmarks.html'
    context_object_name ='bookmarks'

    def get_queryset(self):
        return Bookmark.objects.filter(ispublic=True)


#def all_bookmarks(request):
#   bookmarks = Bookmark.objects.filter(ispublic=True)
#  return render(request, 'bookmark/all_bookmarks.html',{'bookmarks':bookmarks})

#def  bookmark_detail(request, bookmark_id):
# if bookmark_id == '0':
#    return HttpResponseNotFound("Not Found")
# else:
#    return HttpResponse("bookmark id=%s" % bookmark_id)

#def  bookmark_by_user(request, username):
#   user = get_object_or_404(User, username=username)
#  bookmarks = Bookmark.objects.filter(user=user)
# return render(request,'bookmark/detail.html', {'bookmarks':bookmarks,'user':'user'})

class BookmarkByUser(DetailView):
    model = User
    template_name ='bookmark/detail.html'
    content_objects_name = 'user'

    def get_object(self, queryset=None):
        return get_object_or_404(User,username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super(BookmarkByUser,self).get_context_data(**kwargs)
        context['bookmarks'] = Bookmark.objects.filter(user=self.get_object(),ispublic=True)
        return context

class CreateBookmarkView(CreateView):
        form_class = CreateBookmarkForm
        #model =Bookmark
        template_name ='bookmark/create_bookmark_form.html'


        def form_valid(self, form):
            bookmark = form.save(commit=False)
            bookmark.user =self.request.user
            bookmark.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('all-bookmarks'))

        @method_decorator(login_required)
        def dispatch(self, request, *args, **kwargs):
            return super(CreateBookmarkView, self).dispatch(request,*args,**kwargs)

class UpdateBookmarkView(updateView):
    model = Bookmark
    template_name ='bookmark/update_bookmark_form.html'
    fields =['name','url','ispublic','tags']
    sucess_url =reverse('all-bookmarks')


    def get(self,request, *args,**kwargs):
       bookmark =self.get_object()
       if not request.user ==bookmark.user:
           return HttpResponseForbbiden("Forbidden")

       else:
           return super(UpdateBookmarkView, self).get(request, *args,**kwargs)



