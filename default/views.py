from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
#def poll_list(req):
    #polls =poll.objects.all()
    #return render_to_response('poll_list.html', {'items':polls})

class PollList(ListView):
    model= poll

    class PollDetail(DetailView):
        model = Poll