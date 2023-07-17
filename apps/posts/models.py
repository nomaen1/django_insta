from django.db import models
from apps.users.models import User

class StatusModel(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name="Заголовок"
    )
    image = models.ImageField(
        verbose_name="Фото статуса",
        upload_to="media"
    )
    created_at = models.DateField(
        auto_now=True,
        verbose_name="Дата создания"
    )
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        
class Posts(models.Model):
    description = models.TextField(
        verbose_name = "Описание поста"
    )
    location = models.CharField(
        verbose_name="Локация", 
        max_length=50
    )
    
    user = models.ForeignKey(
        User, 
        related_name="user_post", 
        verbose_name="Пользователь", 
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to = "media",
        verbose_name = "Фото поста"
    )    
    
    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name="Пост",
        verbose_name_plural="Посты"
    