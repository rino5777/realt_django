from django.urls import path
from .views import Logining, RegisterUserView, logoutuser,  UserProfile, ChangeUserInfoView, PassChange, AgentProperty, AgentAddProperty,   agentAddProperty, profile_bb_detail
                    

app_name = 'user_profile'

urlpatterns = [

    path('login/', Logining.as_view() ,name='login'), #вход
    path('signup/', RegisterUserView.as_view() ,name='signup'), #регистр
    path('logout/', logoutuser , name='logout'), #выход

    path('profile/', ChangeUserInfoView.as_view() , name='profile'), # профиль
    path('change_password/', PassChange.as_view(),name='change_password'), #изменить пароль

    path('agent_property/', AgentProperty.as_view(),name='agent_property'), #?

    path('agent_add_property/', AgentAddProperty.as_view() ,name='agent_add_property'), #добавить объяв.
    path('property_list/', profile_bb_detail ,name='property_list'),  #список моих объяв.
    
    

]