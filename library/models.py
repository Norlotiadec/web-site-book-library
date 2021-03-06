from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name="Прошел активацию?")
    send_message = models.BooleanField(default=True, verbose_name="Слать сообщения о новых книгах?")

    class Meta(AbstractUser.Meta):
        pass


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Описание', help_text='Напишите что-то...')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)


class Comment(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    comment = models.CharField(max_length=250, help_text='Напишите короткий коментарий', verbose_name='Коментарий')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='статья')

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
