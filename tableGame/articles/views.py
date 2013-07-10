# Create your views here.
# articles/views.py
from django.shortcuts import render_to_response
from articles.models import Article
 
def latest_article(request):
    article_list = Article.objects.order_by('-id')
    return render_to_response('articles/article.html',{'article_list':article_list})
