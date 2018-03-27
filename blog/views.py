from django.shortcuts import render

# Create your views here.
from blog.models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request,article_id):   #①
    article = BlogArticles.objects.get(id=article_id)  #②
    pub = article.publish
    return render(request,"blog/content.html",{"rticle":article,"publish":pub})