from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from django.views.generic.list import ListView
'''
from .models import Error


class ErrorView(ListView):

    model = Error
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
'''
from .models import Error, Event, User2

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_errors = Error.objects.all().count()
    num_instances = Event.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = Event.objects.count()
    
    # The 'all()' is implied by default.    
    num_authors = User2.objects.count()
    
    context = {
        'num_errors': num_errors,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'api/index.html', context=context)
