from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from django.db.models import Count
from .models import Post
# Create your views here.

def index(request):
    object_list = Post.published.all()
    #zooms= Zoom.published.all()[:3]
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'conseil/index.html',{'page': page,'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # List of active comments for this post
    #comments = post.comments.filter(active=True)
    #categories= Category.objects.all()

    # List of similar posts
    #post_tags_ids = post.tags.values_list('id', flat=True)
    #similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    #similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request, 'conseil/detail.html', {'post': post})
