
from django.conf.urls import url
from article import views as article_views


urlpatterns = [
    url(r'^1/$',article_views.basicone),
    url(r'^2/$',article_views.template_two),
    url(r'^3/$',article_views.template_three),
    url(r'^articles/get/(?P<article_id>\d+)/$',article_views.article),
    url(r'^articles/all/$',article_views.articles),
    url(r'^articles/addlike/(?P<article_id>\d+)/$',article_views.addlike),
    url(r'^$',article_views.articles),
]
