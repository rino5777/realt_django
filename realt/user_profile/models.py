from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.



class User(AbstractUser):
    name = models.CharField(max_length=100,  blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank = True)
    date_joined = models.DateTimeField( auto_now_add=True)
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True , verbose_name='Фото профиля ')
    

    class Meta:
        verbose_name = "Прльзователь"
        verbose_name_plural = "Прльзователи"
        
    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('user_profile:login')


    # def get_absolute_url(self):
    #     return f'/profile/{self.id}' 


