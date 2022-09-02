from django.shortcuts import render

from articles.models import TopicArticle, Article, Topic


def articles_list(request):
    template = 'articles/news.html'
    x = Article.objects.all().prefetch_related('mainTopic').all()
    y = Article.objects.all().prefetch_related('mainTopic').all()
    z = Article.objects.all()
    print(x[0].scopes.all()[0])
    print(y)
    print(z)
    context = {
        'object_list': x
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
