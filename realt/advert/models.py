from django.db import models
from user_profile.models import User
from django.urls import reverse
# Create your models here.


class RealtType(models.Model):
    name = models.CharField(max_length=40, verbose_name='тип недвижимости')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Тип недвижимости'


# class Type(models.Model):
#     name = models.CharField(max_length=40, verbose_name='Категория')

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         abstract = True
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
        

class Ads(models.Model):

    #-----------building_freshness
    OLD = 'НОВОЕ'
    NEW = 'ВТОРИЧКА'
    BUILDING_FRESHNESS = [
        (NEW, 'новое здание'),
        (OLD, 'вторичная недвижимость'), ]

    #-----------TRANSACTION_TYPE
    BUY = 'ПОКУПКА'
    RENT = 'АРЕНДА'
    TRANSACTION_TYPE = [
        (BUY, 'покупка'),
        (RENT, 'аренда'), ]

    #------------------------------------------------------фото
    image1 = models.ImageField(blank=True, upload_to= 'media/', 
                              verbose_name='Изображение1')
    image2 = models.ImageField(blank=True, upload_to= 'media/',  
                              verbose_name='Изображение2')
    image3 = models.ImageField(blank=True, upload_to= 'media/',  
                              verbose_name='Изображение3')
    image4 = models.ImageField(blank=True, upload_to= 'media/',  
                              verbose_name='Изображение4')
    image5 = models.ImageField(blank=True, upload_to= 'media/',   
                              verbose_name='Изображение5')
    image6 = models.ImageField(blank=True, upload_to= 'media/',   
                              verbose_name='Изображение6')

    #------------------------------------------------------ описание
    description = models.TextField(verbose_name='Описание')
    #------------------------------------------------------ тип
    rubric = models.CharField(max_length=20, choices= TRANSACTION_TYPE , default= BUY,
                                          verbose_name='Категория ( покупка\продажа )')
    #------------------------------------------------------ тип недвижимости
    realt_type = models.ForeignKey(RealtType, on_delete=models.PROTECT,
                                          verbose_name='Рубрика')
     #------------------------------------------------------ размер общий
    overall_size = models.DecimalField(max_digits=10000, decimal_places=1)
     #------------------------------------------------------ размер жилой
    residential_size = models.DecimalField(max_digits=10000, decimal_places=1)
     #------------------------------------------------------ размер кухни
    kitchen_size = models.DecimalField(max_digits=10000, decimal_places=1)
     #------------------------------------------------------ коллич комнат
    number_of_rooms = models.DecimalField(max_digits=10, decimal_places=1)
     #------------------------------------------------------ этаж
    floor = models.DecimalField(max_digits=10, decimal_places=1)
    #------------------------------------------------------ сколько этажей вообще
    number_of_building = models.DecimalField(max_digits=10, decimal_places=1)
    #------------------------------------------------------ вторичка\новстройка
    building_freshness = models.CharField(max_length=20, choices=BUILDING_FRESHNESS,)
    #------------------------------------------------------ Заголовок
    title = models.CharField(max_length=40, verbose_name='Заголовок')
    #------------------------------------------------------ цена
    price = models.FloatField(default=0, verbose_name='Цена')
    #------------------------------------------------------ Контакты
    contacts = models.CharField(max_length=100, verbose_name='Контакты')
    #------------------------------------------------------ Автор объявления
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор объявления')
    #------------------------------------------------------ Автор объявления                           
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Выводить в списке?')
    #------------------------------------------------------ Опубликовано                                
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликовано')

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('advert:ads', args = [ self.id ] )

    def __str__(self):
        return str(self.title)


class RealtType(models.Model):
    name = models.CharField(max_length=40, verbose_name='тип недвижимости')

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Тип недвижимости'