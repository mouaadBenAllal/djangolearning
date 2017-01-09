from django.views.generic import ListView

from djangoapp.models import Auto


class AutoListView (ListView):
    template_name = 'home.html'
    model = Auto

