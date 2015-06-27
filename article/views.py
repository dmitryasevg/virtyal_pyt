from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from article.form import CommentForm

# Create your views here.
def basicone(request):
    firststr = "first"
    html = "<html><body>This is %s</body></html>" % firststr
    return HttpResponse(html)

def template_two(request):
    view = "Dmitry"
    t = get_template('mytemplate.html')
    html = t.render(Context({'name':view}))
    return HttpResponse(html)

def template_three(request):
    view = "Dmitry 3"
    return render_to_response('mytemplate.html',{'name':view})

def article(request,article_id = 1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id = article_id)
    args['comments'] = Comments.objects.filter(comments_article_id = article_id)
    args['form'] = comment_form
    return render_to_response('article.html',args)

def addcomment(request,article_id):
    return redirect('/')

def articles(request):
    article = Article.objects.all()
    return render_to_response('articles.html',{'articles':article})

def addlike(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
        article.article_likes +=1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

