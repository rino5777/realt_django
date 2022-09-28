from django.urls import path
from .views import Logining, RegisterUserView, logoutuser,  UserProfile, ChangeUserInfoView, PassChange

app_name = 'user_profile'

urlpatterns = [

    path('login/', Logining.as_view() ,name='login'),
    path('signup/', RegisterUserView.as_view() ,name='signup'),
    path('logout/', logoutuser , name='logout'),

    path('profile/', ChangeUserInfoView.as_view() , name='profile'),
    path('change_password/', PassChange.as_view(),name='change_password'),
    
    

]