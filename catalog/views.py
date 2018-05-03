from django.shortcuts import render
from .models import Dress, Guest, DressInstance, Brand

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_dress=Dress.objects.all().count()
    num_instances=DressInstance.objects.all().count()
    # Available dress (status = 'a')
    num_instances_season=DressInstance.objects.filter(status__exact='a').count()
    num_guest=Guest.objects.count()  # The 'all()' is implied by default.
	

   # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
	
	
	
   # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_dress':num_dress,'num_instances':num_instances,'num_instances_season':num_instances_season,'num_guest':num_guest},
    )
from django.views import generic

class DressListView(generic.ListView):
    model = Dress
    paginate_by = 2
class DressDetailView(generic.DetailView):
    model = Dress
class GuestListView(generic.ListView):
    model = Guest
    paginate_by = 2
class GuestDetailView(generic.DetailView):
    model = Guest