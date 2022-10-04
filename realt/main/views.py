from django.views.generic.base import TemplateView
from advert.models import Ads, RealtType
from user_profile.models import User
# Create your views here.



class Main(TemplateView):
    template_name = 'main/main.html'
    

    def get(self, request, *args, **kwargs):
        self.object = User.objects.all()
        self.plugs = Ads.objects.all()
        self.type = RealtType.objects.all()
        self.user = request.user
        return super().get(request, *args, **kwargs)
            
    def get_context_data(self, **kwargs):
        us = User.objects.all()
        context = super().get_context_data(**kwargs)
    
        context['publisher'] = self.object
        context['user'] = self.user
        context['plugs'] = self.plugs
        context['types'] = self.type
        return context

    def get_queryset(self):
        return self.object.all()