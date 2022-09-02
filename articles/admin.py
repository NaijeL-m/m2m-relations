from django.contrib import admin
from .models import Article, Topic, TopicArticle

class TopicArticleInLine(admin.TabularInline):
    model = TopicArticle
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']
    list_filter = ['published_at']
    inlines = [TopicArticleInLine]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
