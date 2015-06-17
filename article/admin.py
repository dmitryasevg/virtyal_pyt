from django.contrib import admin

from article.models import Article, Comments

# Register your models here.
class AdminInline(admin.StackedInline):
    model = Comments
    extra = 2

class AdminArticle(admin.ModelAdmin):
    fields = ['article_title','article_text','article_date']
    inlines = [AdminInline]



admin.site.register(Article, AdminArticle)