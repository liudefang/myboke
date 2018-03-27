from django.contrib import admin
from blog.models import BlogArticles     # ①


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ('title', "body")
    ordering = ['publish', 'author']


admin.site.register(BlogArticles)     #②
