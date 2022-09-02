from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тема')


    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Topic, related_name='articles', through='TopicArticle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



class TopicArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='mainTopic')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='mainTopic')
    is_main = models.BooleanField()