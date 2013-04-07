from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.models import Post


def index(request):
    posts = Post.all().order('-created_at')
    return render_to_response('index.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post(title=title,
                    body=body)
        print post.put()

        return HttpResponseRedirect('/post/' + str(post.key().id()))
    else:
        return render_to_response('create.html',
                                  {},
                                  context_instance=RequestContext(request))


def details(request, post_id):
    post = Post.get_by_id(int(post_id))

    return render_to_response('details.html', {'post': post})
