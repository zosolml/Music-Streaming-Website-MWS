from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import song_thumb,Comment
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import CommentForm
# Create your views here.

class SongListView(ListView):
    model=song_thumb
    context_object_name='posts'
    paginate_by=3
    template_name='songlist.html'

def song_detail(request, year, month, day, post):
    post = get_object_or_404(song_thumb, slug=post,

                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
            comment_form = CommentForm()
    return render(request,'musicplayer.html',{'post': post,'comments': comments,'new_comment': new_comment,'comment_form': comment_form})



def search(request):
    query=request.GET['q']
    allposts=song_thumb.objects.filter(song_title__icontains=query)
    params={'allposts':allposts}
    return render(request,searchengine.html,params)
