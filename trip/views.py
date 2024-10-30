from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Trip


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips
    }
    return render(request, 'trip_list.html', context)


