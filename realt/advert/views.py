from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Ads

# Create your views here.

class Property_detail(TemplateView):
    template_name = 'property/property-detail-2.html'

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['ads'] = get_object_or_404(Ads, id = self.kwargs['id'] )
        context['is_user'] = self.request.user
        return context

def plug(request, id):
    plug = get_object_or_404(Ads, id = id )
    is_user = request.user

    context = {'plug_one': plug, 'is_user': is_user }
    return render(request, 'plug/plug.html', context)