from django.urls import path
from .views import  Property_detail

app_name = 'advert'

urlpatterns = [
    path('<int:id>/', Property_detail.as_view() ,name='ads'),
    

]