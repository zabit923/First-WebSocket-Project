from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ChatGroup(models.Model):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    group_name = models.CharField(
        'Группа',
        max_length=128,
        unique=True
    )

    users_online = models.ManyToManyField(
        User,
        related_name='online_in_groups',
        blank=True
    )

    def __str__(self):
        return f'{self.group_name}'


class GroupMessage(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']

    group = models.ForeignKey(
        ChatGroup,
        related_name='chat_messages',
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        User,
        related_name='messages',
        on_delete=models.CASCADE
    )

    body = models.CharField('Текст', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} : {self.body}'
